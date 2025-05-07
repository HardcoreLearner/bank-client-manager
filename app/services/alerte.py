from datetime import datetime
import pandas as pd

def verifier_depassement(compte, historique_operations: pd.DataFrame) -> dict:
    """
    Détecte les dépassements de plafond pour un compte donné.
    """
    alerts = {}

    # Vérification solde
    if compte.solde > compte.plafond_solde:
        alerts['solde'] = f"Dépassement du plafond de solde ({compte.solde} > {compte.plafond_solde})"

    # Calcul du total mensuel
    now = datetime.now()
    operations_mois = historique_operations[
        (historique_operations['compte_id'] == compte.id) &
        (pd.to_datetime(historique_operations['date_operation']).dt.month == now.month)
    ]

    total_mensuel = operations_mois['montant'].sum()
    if total_mensuel > compte.plafond_mensuel:
        alerts['mensuel'] = f"Dépassement du plafond mensuel ({total_mensuel} > {compte.plafond_mensuel})"

    return alerts