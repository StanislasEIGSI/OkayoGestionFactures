# Okayo API – Gestion de Factures avec FastAPI

Bienvenue dans l'API de gestion de factures de la société fictive **Okayo**, développée en **Python** avec le framework **FastAPI**.  
Ce projet permet de gérer les **clients**, **produits**, **factures**, **lignes de facture**, et les informations de l’entreprise Okayo.

---

##  Fonctionnalités

-  Création, consultation, mise à jour et suppression de **clients**
-  Gestion des **produits** avec historique des prix et taux de TVA
-  Création de **factures** associées à des clients
-  Ajout de **lignes de facture** avec quantité et prix
-  Consultation d’une facture complète avec ses lignes
-  Documentation interactive via Swagger UI

---

##  Structure du projet
okayo_api/
│
├── app/
│   ├── main.py            # Point d'entrée de l'application
│   ├── database.py        # Connexion à la base de données
│   ├── models.py          # Modèles SQLAlchemy
│   ├── schemas.py         # Schémas Pydantic
│   └── crud/              # (Optionnel) Fonctions métiers
│
├── venv/                  # Environnement virtuel
└── README.md

## Utilisation de l'API:

1. Cloner le dépôt

  git clone https://github.com/votre-utilisateur/okayo_api.git
  cd okayo_api

2. Créer un environnement virtuel

  python -m venv venv
  source venv/bin/activate  # ou venv\Scripts\activate sous Windows

3. Installer les dépendances

  pip install fastapi uvicorn sqlalchemy pydantic

4. Lancer l'application

  uvicorn main:app --reload
  Accès à la documentation interactive : http://127.0.0.1:8000/docs

