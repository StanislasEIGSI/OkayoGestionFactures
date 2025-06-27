from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# === CLIENTS ===
class ClientBase(BaseModel):
    nom: str
    adresse: str
    contact_mail: str
    contact_tel: str
    date_debut: date
    date_fin: Optional[date] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    code_client: int
    class Config:
        orm_mode = True

# === PRODUITS ===
class ProduitBase(BaseModel):
    nom: str
    prix_ht: float
    date_debut_validite: date
    date_fin_validite: Optional[date] = None
    taux_TVA: float

class ProduitCreate(ProduitBase):
    pass

class Produit(ProduitBase):
    id_produit: int
    class Config:
        orm_mode = True

# === LIGNES FACTURE ===
class LigneFactureBase(BaseModel):
    id_produit: int
    quantite: int

class LigneFactureCreate(LigneFactureBase):
    ref_facture: int

class LigneFacture(LigneFactureBase):
    id_ligne: int
    class Config:
        orm_mode = True

# === FACTURES ===
class FactureBase(BaseModel):
    code_client: int
    date_creation: date
    date_echeance: date
    nom: str

class FactureCreate(FactureBase):
    pass

class Facture(FactureBase):
    ref_facture: int
    lignes: List[LigneFacture] = []
    class Config:
        orm_mode = True
