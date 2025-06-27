from sqlalchemy.orm import Session
import models, schemas

# === Clients ===
def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Clients(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session):
    return db.query(models.Clients).all()

# === Produits ===
def create_produit(db: Session, produit: schemas.ProduitCreate):
    db_produit = models.InfoProduits(**produit.dict())
    db.add(db_produit)
    db.commit()
    db.refresh(db_produit)
    return db_produit

def get_produits(db: Session):
    return db.query(models.InfoProduits).all()

# === Factures ===
def create_facture(db: Session, facture: schemas.FactureCreate):
    db_facture = models.Factures(**facture.dict())
    db.add(db_facture)
    db.commit()
    db.refresh(db_facture)
    return db_facture

def get_factures(db: Session):
    return db.query(models.Factures).all()

def get_facture_by_id(db: Session, id: int):
    return db.query(models.Factures).filter(models.Factures.ref_facture == id).first()

# === Lignes de facture ===
def create_ligne_facture(db: Session, ligne: schemas.LigneFactureCreate):
    db_ligne = models.LignesFacture(**ligne.dict())
    db.add(db_ligne)
    db.commit()
    db.refresh(db_ligne)
    return db_ligne

def get_lignes_facture(db: Session, ref_facture: int):
    return db.query(models.LignesFacture).filter(models.LignesFacture.ref_facture == ref_facture).all()
