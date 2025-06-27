from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Clients(Base):
    __tablename__ = "clients"
    code_client = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    adresse = Column(String)
    contact_mail = Column(String)
    contact_tel = Column(String)
    date_debut = Column(Date)
    date_fin = Column(Date, nullable=True)

    factures = relationship("Factures", back_populates="client")


class InfoProduits(Base):
    __tablename__ = "info_produits"
    id_produit = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prix_ht = Column(Float)
    date_debut_validite = Column(Date)
    date_fin_validite = Column(Date, nullable=True)
    taux_TVA = Column(Float)


class Factures(Base):
    __tablename__ = "factures"
    ref_facture = Column(Integer, primary_key=True, index=True)
    code_client = Column(Integer, ForeignKey("clients.code_client"))
    date_creation = Column(Date)
    date_echeance = Column(Date)
    nom = Column(String)

    client = relationship("Clients", back_populates="factures")
    lignes = relationship("LignesFacture", back_populates="facture")


class LignesFacture(Base):
    __tablename__ = "lignes_facture"
    id_ligne = Column(Integer, primary_key=True, index=True)
    ref_facture = Column(Integer, ForeignKey("factures.ref_facture"))
    id_produit = Column(Integer, ForeignKey("info_produits.id_produit"))
    quantite = Column(Integer)

    facture = relationship("Factures", back_populates="lignes")
    produit = relationship("InfoProduits")
