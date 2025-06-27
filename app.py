import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Gestion des Factures")

# Afficher les clients
if st.button("Afficher les clients"):
    resp = requests.get(f"{API_URL}/clients/")
    st.write(resp.json())

# Ajouter un client
st.header("Ajouter un client")
code = st.text_input("Code client")
nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
if st.button("Créer le client"):
    data = {"code_client": code, "nom": nom, "prenom": prenom}
    resp = requests.post(f"{API_URL}/clients/", json=data)
    st.write(resp.json())

# Ajouter une facture
st.header("Ajouter une facture")
code_facture = st.text_input("Code facture")
code_client_facture = st.text_input("Code client pour la facture")
date_facture = st.text_input("Date de la facture (YYYY-MM-DD)")
if st.button("Créer la facture"):
    data = {
        "code_facture": code_facture,
        "code_client": code_client_facture,
        "date_facture": date_facture
    }
    resp = requests.post(f"{API_URL}/factures/", json=data)
    st.write(resp.json())