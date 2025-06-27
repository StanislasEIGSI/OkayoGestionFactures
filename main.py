from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dépendance à la base
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === Clients ===
@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db, client)

@app.get("/clients/", response_model=list[schemas.Client])
def read_clients(db: Session = Depends(get_db)):
    return crud.get_clients(db)

# === Produits ===
@app.post("/produits/", response_model=schemas.Produit)
def create_produit(produit: schemas.ProduitCreate, db: Session = Depends(get_db)):
    return crud.create_produit(db, produit)

@app.get("/produits/", response_model=list[schemas.Produit])
def read_produits(db: Session = Depends(get_db)):
    return crud.get_produits(db)

# === Factures ===
@app.post("/factures/", response_model=schemas.Facture)
def create_facture(facture: schemas.FactureCreate, db: Session = Depends(get_db)):
    return crud.create_facture(db, facture)

@app.get("/factures/", response_model=list[schemas.Facture])
def read_factures(db: Session = Depends(get_db)):
    return crud.get_factures(db)

@app.get("/factures/{facture_id}", response_model=schemas.Facture)
def read_facture(facture_id: int, db: Session = Depends(get_db)):
    facture = crud.get_facture_by_id(db, facture_id)
    if not facture:
        raise HTTPException(status_code=404, detail="Facture introuvable")
    return facture

# === Lignes de facture ===
@app.post("/lignes/", response_model=schemas.LigneFacture)
def create_ligne_facture(ligne: schemas.LigneFactureCreate, db: Session = Depends(get_db)):
    return crud.create_ligne_facture(db, ligne)

@app.get("/lignes/{ref_facture}", response_model=list[schemas.LigneFacture])
def read_lignes_facture(ref_facture: int, db: Session = Depends(get_db)):
    return crud.get_lignes_facture(db, ref_facture)
