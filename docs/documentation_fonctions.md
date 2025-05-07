# Documentation des Fonctions

## 1. Fonction `construire_classificateur_risque`

### Description
Cette fonction construit un classificateur de risque en utilisant Random Forest pour prédire les clients à risque en fonction de leurs caractéristiques financières.

### Paramètres
- **df** : pandas.DataFrame
    - Le DataFrame contenant les informations des clients, y compris 'solde', 'decouvert_autorise', 
    'montant_verse_mensuel', 'montant_preleve_mensuel', 'nombre_transactions', 'solde_moyen'.
  
### Retourne
- **rf** : sklearn.ensemble.RandomForestClassifier
    - Le modèle Random Forest entraîné.
- **accuracy** : float
    - La précision (accuracy) du modèle sur les données de test.
- **report** : str
    - Le rapport de classification qui inclut des mesures comme la précision, le rappel, et le F1-score.

### Exemple
```python
rf, accuracy, report = construire_classificateur_risque(df)
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{report}")
```

## 2. Fonction `segmenter_clients_par_kmeans`

### Description
Cette fonction segmente les clients en utilisant le clustering KMeans basé sur leurs caractéristiques financières telles que le solde moyen, le nombre de transactions et le nombre de découverts.

### Paramètres
- **df_comptes** : pandas.DataFrame
- **n_clusters** : int, optionnel (par défaut 4) 
  
### Retourne
- **df_comptes** : pandas.DataFrame
- **kmeans** : sklearn.cluster.KMeans

### Exemple
```python
df_comptes_segmenté, kmeans = segmenter_clients_par_kmeans(df_comptes)
print(df_comptes_segmenté.head())
```
