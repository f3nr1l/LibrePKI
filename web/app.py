from flask import Flask, render_template

app = Flask(__name__)

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

@app.route("/generate")
def generate_cert():
    return render_template("generate.html")

@app.route("/upload")
def upload_cert():
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
