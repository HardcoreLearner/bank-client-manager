from fastapi import APIRouter, HTTPException
from app.models.schemas import CompteCreate, RapportClient
from app.services.portefeuille import ajouter_compte, mettre_a_jour_portefeuille, generer_rapport

router = APIRouter()

@router.post("/compte/ajouter")
def ajouter_nouveau_compte(compte: CompteCreate):
    return ajouter_compte(compte)

@router.put("/portefeuille/{client_id}")
def maj_portefeuille(client_id: str, compte: CompteCreate):
    return mettre_a_jour_portefeuille(client_id, compte)

@router.get("/rapport/{client_id}", response_model=RapportClient)
def rapport_client(client_id: str):
    rapport = generer_rapport(client_id)
    if not rapport:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return rapport
