import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

def construire_classificateur_risque(df):
    """
    Construire un classificateur de risque utilisant Random Forest pour prédire si un client est à risque.
    
    Cette fonction crée une étiquette binaire de risque basée sur le solde du client et sur son découvert autorisé.
    Ensuite, elle utilise un modèle RandomForest pour prédire les clients à risque en fonction de certaines caractéristiques.

    Paramètres :
    -----------
    df : pandas.DataFrame
        DataFrame contenant les données des clients, avec des colonnes telles que 'solde', 'decouvert_autorise', 
        'montant_verse_mensuel', 'montant_preleve_mensuel', 'nombre_transactions', et 'solde_moyen'.
        
    Retourne :
    ---------
    rf : sklearn.ensemble.RandomForestClassifier
        Le modèle Random Forest entraîné.
    accuracy : float
        La précision (accuracy) du modèle sur les données de test.
    report : str
        Le rapport de classification, comprenant des mesures de performance comme la précision, le rappel, et le F1-score.

    Exemple :
    ---------
    rf, accuracy, report = construire_classificateur_risque(df)
    print(f"Accuracy: {accuracy}")
    print(f"Classification Report:\n{report}")
    """
    # Créer une étiquette de risque (par exemple, solde inférieur à 0 ou découvert autorisé)
    df["is_risky"] = (df["solde"] < 0) | (df["solde"] < df["decouvert_autorise"])

    # Définir les caractéristiques (features) et l'étiquette (label)
    X = df[["solde", "montant_verse_mensuel", "montant_preleve_mensuel", "nombre_transactions", "solde_moyen"]]
    y = df["is_risky"]

    # Normaliser les données
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Diviser les données en ensembles d'entraînement et de test (80% / 20%)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Créer le classificateur RandomForest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)

    # Entraîner le modèle
    rf.fit(X_train, y_train)

    # Prédire les résultats sur l'ensemble de test
    y_pred = rf.predict(X_test)

    # Évaluation du modèle
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return rf, accuracy, report
