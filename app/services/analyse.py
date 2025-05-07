import pandas as pd
from datetime import datetime

def calcul_score_risque_par_transactions(compte_id: str, historique: pd.DataFrame) -> float:
    df = historique[historique["compte_id"] == compte_id].copy()

    if df.empty:
        return 100.0  # Aucun historique = risque maximal

    df["date_operation"] = pd.to_datetime(df["date_operation"])
    df["mois"] = df["date_operation"].dt.to_period("M")

    # 1. Nombre de mois avec solde < 0
    solde_mensuel = df.groupby("mois")["montant"].sum().cumsum()
    mois_decouvert = (solde_mensuel < 0).sum()

    score_decouvert = min(mois_decouvert / 3, 1.0) * 40

    # 2. Volatilité mensuelle (écart type / moyenne)
    flux_mensuel = df.groupby("mois")["montant"].sum()
    if flux_mensuel.mean() != 0:
        volatilite = (flux_mensuel.std() / abs(flux_mensuel.mean()))
    else:
        volatilite = 1.0
    score_volatilite = min(volatilite, 1.0) * 30

    # 3. Inactivité : mois sans transaction
    tous_mois = pd.period_range(df["mois"].min(), df["mois"].max(), freq="M")
    mois_inactifs = len(tous_mois) - df["mois"].nunique()
    score_inactivite = min(mois_inactifs / 3, 1.0) * 20

    # 4. Placeholder pour détection d’activité suspecte
    score_suspect = 0  # À affiner plus tard

    score_total = round(score_decouvert + score_volatilite + score_inactivite + score_suspect, 2)
    return min(score_total, 100.0)