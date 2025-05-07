from pydantic import BaseModel
from typing import Optional

class CompteCreate(BaseModel):
    client_id: str
    nom_complet: str
    type_compte: str
    solde: float
    plafond: float
    plafond_solde: Optional[float] = 10_000_000
    plafond_mensuel: Optional[float] = 20_000_000
    decouvert_autorise: str
    montant_verse_mensuel: float
    montant_preleve_mensuel: float
    nombre_transactions: int
    date_ouverture: str
    statut_client: str
    note_rentabilite: int
    segment: str
    score_risque: float

class RapportClient(BaseModel):
    client_id: str
    nom_complet: str
    solde_total: float
    segment: str
    score_risque: float
    note_rentabilite: int
