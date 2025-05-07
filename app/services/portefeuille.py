from app.models.schemas import CompteCreate, RapportClient
import pandas as pd
import os

DATA_PATH = "data/comptes_portefeuille.csv"

def _charger_donnees() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)

def _sauvegarder_donnees(df: pd.DataFrame):
    df.to_csv(DATA_PATH, index=False)

def ajouter_compte(compte: CompteCreate):
    df = _charger_donnees()
    new_row = compte.model_dump()
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    _sauvegarder_donnees(df)
    return {"message": "Compte ajouté avec succès."}

def mettre_a_jour_portefeuille(client_id: str, compte: CompteCreate):
    df = _charger_donnees()
    if client_id not in df["client_id"].values:
        return {"message": "Client introuvable."}

    df.loc[df["client_id"] == client_id] = compte.model_dump()
    _sauvegarder_donnees(df)
    return {"message": "Portefeuille mis à jour."}

def generer_rapport(client_id: str) -> RapportClient | None:
    df = _charger_donnees()
    client = df[df["client_id"] == client_id]
    if client.empty:
        return None

    total_solde = client["solde"].sum()
    row = client.iloc[0]

    return RapportClient(
        client_id=row["client_id"],
        nom_complet=row["nom_complet"],
        solde_total=total_solde,
        segment=row["segment"],
        score_risque=row["score_risque"],
        note_rentabilite=row["note_rentabilite"]
    )
def calcul_score_risque(solde: float, plafond: float) -> float:
    if plafond == 0:
        return 1.0
    score = min(1.0, max(0.0, abs(solde) / plafond))
    return score


def calcul_note_rentabilite(verse: float, preleve: float) -> float:
    if verse == 0:
        return 0
    ratio = (verse - preleve) / verse
    note = max(0, min(100, ratio * 100))
    return round(note, 2)
