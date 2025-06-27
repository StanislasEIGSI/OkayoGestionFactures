import requests

base_url = "http://127.0.0.1:8000"

# Création des clients
clients = [
    {"code_client": "C001", "nom": "Dupont", "prenom": "Jean"},
    {"code_client": "C002", "nom": "Martin", "prenom": "Claire"},
    {"code_client": "C003", "nom": "Durand", "prenom": "Paul"},
]

# Création des produits
produits = [
    {"code_produit": "P001", "designation": "Ordinateur", "prix_unitaire": 1200.0},
    {"code_produit": "P002", "designation": "Imprimante", "prix_unitaire": 200.0},
]

# Création des factures (une par client)
factures = [
    {"code_facture": "F001", "code_client": "C001", "date_facture": "2024-06-25"},
    {"code_facture": "F002", "code_client": "C002", "date_facture": "2024-06-25"},
    {"code_facture": "F003", "code_client": "C003", "date_facture": "2024-06-25"},
]

# Création des lignes de facture (une par facture)
lignes_facture = [
    {"code_facture": "F001", "code_produit": "P001", "quantite": 1},
    {"code_facture": "F002", "code_produit": "P002", "quantite": 2},
    {"code_facture": "F003", "code_produit": "P001", "quantite": 1},
]

# Création des clients
for client in clients:
    requests.post(f"{base_url}/clients/", json=client)

# Création des produits
for produit in produits:
    requests.post(f"{base_url}/produits/", json=produit)

# Création des factures
for facture in factures:
    requests.post(f"{base_url}/factures/", json=facture)

# Création des lignes de facture
for ligne in lignes_facture:
    requests.post(f"{base_url}/lignes_facture/", json=ligne)

print("Base de test initialisée !")