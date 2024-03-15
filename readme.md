# Prêt Prediction Project

Ce projet vise à développer un système de prédiction de prêts à l'aide de modèles d'apprentissage automatique. Il est divisé en deux parties principales : une API construite avec FastAPI pour le back-end et une application Web Django pour le front-end.

## Contenu du Projet

Le projet est organisé en deux grandes parties :

1. **API (FastAPI)** :
   - Dossiers de notebooks pour le nettoyage, l'EDA (Exploratory Data Analysis) et la modélisation.
   - Implémentation d'une API utilisant FastAPI pour servir les prédictions de prêt.

2. **Application Web (Django)** :
   - Trois applications distinctes :
     - `main` : Pages accessibles sans connexion, avec des fonctionnalités d'affichage.
     - `functionalities` : Pages nécessitant une connexion, telles que le formulaire de prédiction de prêt.
     - `accounts` : Gestion de l'inscription, de la connexion, des emails de confirmation et de la réinitialisation du mot de passe utilisant Mailjet.

## Installation

### Avec Docker Compose

1. Assurez-vous d'avoir Docker et Docker Compose installés sur votre système.
2. Clonez ce dépôt.
3. Naviguez vers le répertoire racine du projet.
4. Exécutez `docker-compose up -d --build` pour construire et lancer les conteneurs.

### Sans Docker Compose

Si vous préférez ne pas utiliser Docker Compose, vous pouvez exécuter chaque composant individuellement. Consultez les README dans les dossiers `API` et `Web` pour des instructions détaillées.

## Déploiement

1. Assurez-vous d'avoir Docker installé et connecté à Docker Hub.
2. Exécutez le script `deploy.sh` pour construire et pousser les images Docker vers Docker Hub.
3. Pour le déploiement sur Azure, assurez-vous d'avoir un compte Azure et le CLI Azure installé.
4. Utilisez le CLI Azure pour déployer les conteneurs sur Azure Container Instances ou Azure Kubernetes Service, selon vos besoins.


## Lien du Dataset utilisé

https://drive.google.com/file/d/1vdNaWcJgMzUnlaDVA4FuZRFYinO8UsPQ/view?usp=drive_link


## Génération des Données et Modèles

### Génération des Données

Pour générer les datasets et modèles, veuillez suivre les instructions ci-dessous :

1. Ouvrez le notebook `0_Cleaning.ipynb` situé dans le répertoire `api/Model_pret/Modelisation/` pour effectuer le nettoyage des données.

2. Suivez les étapes nécessaires dans les notebooks `2_` et `3_` pour la génération des données et des modèles respectivement, situés dans le répertoire `api/Model_pret/Modelisation/`.

### Configuration du Fichier .env

Pour configurer votre fichier `.env` pour le projet Web, veuillez inclure les variables suivantes :

```dotenv
SECRET_KEY=Votre_Cle_Secrete
DEBUG=True # Ou False en production
API_KEY=Votre_Cle_API
MAILJET_SECRET_KEY=Votre_Cle_Secrete_Mailjet
MAILJET_API_KEY=Votre_Cle_API_Mailjet
MAILJET_SENDER=Votre_Adresse_Email_Mailjet
FRONTEND_URL=URL_de_votre_application_Frontend
POSTGRES_DB=Nom_de_votre_base_de_données
POSTGRES_PASSWORD=Votre_Mot_de_Passe_PostgreSQL
POSTGRES_USER=Votre_Utilisateur_PostgreSQL
POSTGRES_HOST=Adresse_de_votre_hôte_PostgreSQL
POSTGRES_PORT=Port_de_votre_base_de_données_PostgreSQL
POSTGRES_RDY=True # Ou False pour indiquer l'état prêt de votre base de données PostgreSQL
Assurez-vous de remplacer les valeurs fictives par vos propres valeurs dans le fichier .env.