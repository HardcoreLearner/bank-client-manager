import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def segmenter_clients_par_kmeans(df_comptes: pd.DataFrame, n_clusters: int = 4):
    """
    Segmenter les clients en utilisant le clustering KMeans en fonction de leurs caractéristiques financières.

    Cette fonction applique le clustering KMeans pour regrouper les clients en segments en fonction de leur solde moyen, 
    du nombre de transactions, et du nombre de découverts. Les clients seront ensuite assignés à un segment en fonction
    de leurs caractéristiques.

    Paramètres :
    -----------
    df_comptes : pandas.DataFrame
        Le DataFrame contenant les informations des clients, avec des colonnes comme 'solde_moyen', 
        'nb_transactions', 'nb_decouverts'.
        
    n_clusters : int, optionnel (par défaut 4)
        Le nombre de clusters à générer lors de l'application de KMeans.

    Retourne :
    ---------
    df_comptes : pandas.DataFrame
        Le DataFrame mis à jour avec une nouvelle colonne 'segment' qui contient le numéro de segment attribué à chaque client.
    kmeans : sklearn.cluster.KMeans
        L'instance de KMeans entraînée.

    Exemple :
    ---------
    df_comptes_segmenté, kmeans = segmenter_clients_par_kmeans(df_comptes)
    print(df_comptes_segmenté.head())
    """
    # Colonnes d'intérêt
    features = ["solde_moyen", "nb_transactions", "nb_decouverts"]

    # Prétraitement
    scaler = StandardScaler()
    X = scaler.fit_transform(df_comptes[features])

    # Clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df_comptes["segment"] = kmeans.fit_predict(X)

    return df_comptes, kmeans
