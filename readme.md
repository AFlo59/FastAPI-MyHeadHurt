Prêt Prediction Project
Ce projet vise à développer un système de prédiction de prêts à l'aide de modèles d'apprentissage automatique. Il est divisé en deux parties principales : une API construite avec FastAPI pour le back-end et une application Web Django pour le front-end.

Contenu du Projet
Le projet est organisé en deux grandes parties :

API (FastAPI) :

Dossiers de notebooks pour le nettoyage, l'EDA (Exploratory Data Analysis) et la modélisation.
Implémentation d'une API utilisant FastAPI pour servir les prédictions de prêt.
Application Web (Django) :

Trois applications distinctes :
main : Pages accessibles sans connexion, avec des fonctionnalités d'affichage.
functionalities : Pages nécessitant une connexion, telles que le formulaire de prédiction de prêt.
accounts : Gestion de l'inscription, de la connexion, des emails de confirmation et de la réinitialisation du mot de passe utilisant Mailjet.
Installation
Avec Docker Compose
Assurez-vous d'avoir Docker et Docker Compose installés sur votre système.
Clonez ce dépôt.
Naviguez vers le répertoire racine du projet.
Exécutez docker-compose up -d --build pour construire et lancer les conteneurs.
Sans Docker Compose
Si vous préférez ne pas utiliser Docker Compose, vous pouvez exécuter chaque composant individuellement. Consultez les README dans les dossiers API et Web pour des instructions détaillées.

Déploiement
Assurez-vous d'avoir Docker installé et connecté à Docker Hub.
Exécutez le script deploy.sh pour construire et pousser les images Docker vers Docker Hub.
Pour le déploiement sur Azure, assurez-vous d'avoir un compte Azure et le CLI Azure installé.
Utilisez le CLI Azure pour déployer les conteneurs sur Azure Container Instances ou Azure Kubernetes Service, selon vos besoins.