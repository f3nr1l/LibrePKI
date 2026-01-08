# LibrePKI

Une application Dockerisée pour gérer une PKI (Public Key Infrastructure) avec CFSSL.

## Fonctionnalités
- Génération de certificats racine, intermédiaires, serveur et client.
- Interface web moderne et responsive.
- Intégration facile avec Docker.

## Prérequis
- Docker
- Docker Compose

## Installation
1. Cloner ce dépôt.
2. Builder les images :
   ```bash
   docker-compose build
3. Démarrer les conteneurs :
   ```bash
   docker-compose up
4. Accéder à l'interface sur http://localhost:5000.
