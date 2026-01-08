from flask import Flask, render_template, request, flash, redirect, url_for
import subprocess
import json
import os

app = Flask(__name__)
app.secret_key = 'temporary_secret_key'  # À remplacer par une clé sécurisée en production

# Données fictives pour les placeholders
CERTS = [
    {"id": 1, "name": "Certificat Racine (Intermédiaire)", "type": "intermediate", "status": "Valide", "expires": "2026-12-31"},
    {"id": 2, "name": "Certificat Serveur (librepki.example.com)", "type": "server", "status": "Valide", "expires": "2025-12-31"},
    {"id": 3, "name": "Certificat Client (Utilisateur 1)", "type": "client", "status": "Valide", "expires": "2025-06-30"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/certs")
def list_certs():
    return render_template("certs.html", certs=CERTS)

@app.route("/generate", methods=["GET", "POST"])
def generate_cert():
    if request.method == "POST":
        cert_type = request.form.get("type")
        common_name = request.form.get("common_name")

        # Créer un fichier CSR temporaire
        csr_json = {
            "CN": common_name,
            "hosts": [common_name],
            "key": {"algo": "rsa", "size": 2048},
            "names": [{"O": "LibrePKI"}]
        }

        with open("/tmp/csr.json", "w") as f:
            json.dump(csr_json, f)

        # Appeler CFSSL pour générer le certificat
        cmd = [
            "cfssl", "gencert",
            "-ca", "/data/ca.pem",
            "-ca-key", "/data/ca-key.pem",
            "-config", "/data/config.json",
            "-profile", cert_type,
            "/tmp/csr.json"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            flash("Certificat généré avec succès !", "success")
            # Sauvegarder le certificat généré
            cert_filename = f"/data/certs/{common_name}.pem"
            os.makedirs("/data/certs", exist_ok=True)  # Créer le dossier s'il n'existe pas
            with open(cert_filename, "w") as f:
                f.write(result.stdout)
            # Ajouter le certificat à la liste CERTS
            CERTS.append({
                "id": len(CERTS) + 1,
                "name": f"Certificat {cert_type} ({common_name})",
                "type": cert_type,
                "status": "Valide",
                "expires": "2026-12-31"  # À remplacer par la date réelle du certificat
            })
        else:
            flash(f"Erreur lors de la génération : {result.stderr}", "error")

        return redirect(url_for("list_certs"))

    return render_template("generate.html")

@app.route("/upload")
def upload_cert():
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
