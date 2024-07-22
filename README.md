Projet de Modernisation de la Signature Électronique pour le Groupe UDEV-2
Description
Ce projet vise à moderniser et à rendre plus accessible le processus de signature électronique quotidienne pour les étudiantes du groupe UDEV-2 à l'université. Utilisant Docker pour l'orchestration, PostgreSQL pour le stockage des données, pgAdmin4 pour l'administration de la base de données, Nginx comme reverse proxy, et Flask pour le développement de l'application web, ce projet offre une solution robuste et moderne pour la gestion des signatures électroniques.
Table des Matières : 

Description
Prérequis
Installation
Utilisation
Structure du Projet

Licence


Prérequis : 
Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

Docker
Docker Compose


Installation : 

Clonez ce dépôt : 





Utilisation

Accédez à l'interface utilisateur via votre navigateur web à l'adresse http://localhost:8080.
Remplissez le formulaire de signature électronique et soumettez-le.
Les données seront enregistrées dans la base de données PostgreSQL et sauvegardées dans un fichier Excel.
Structure du Projet
docker-compose.yml: Configuration de Docker Compose pour orchestrer les services.
nginx.conf: Configuration de Nginx pour le routage des requêtes.
backend/: Contient l'application Flask.
app.py: Code de l'application Flask pour gérer les soumissions.
index.html: Page HTML pour l'interface utilisateur.
requirements.txt: Liste des dépendances Python.
Dockerfile: Fichier Docker pour construire l'image de l'application Flask.


Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
