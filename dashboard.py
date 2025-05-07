import pandas as pd
import streamlit as st

# Chargement des données
@st.cache_data
def charger_donnees():
    df = pd.read_csv("data/comptes_portefeuille.csv")

    # Conversion en float
    df["solde"] = pd.to_numeric(df["solde"], errors="coerce")
    df["decouvert_autorise"] = pd.to_numeric(df["decouvert_autorise"], errors="coerce")

    return df

df = charger_donnees()

# Création de l'étiquette de risque
df["is_risky"] = (df["solde"] < 0) | (df["solde"] < df["decouvert_autorise"])

# Synthèse générale
st.title("Tableau de bord des comptes clients")

col1, col2, col3 = st.columns(3)
col1.metric("Nombre total de clients", len(df))
col2.metric("Clients à risque", df["is_risky"].sum())
col3.metric("Solde moyen global", f"{df['solde'].mean():.2f} FCFA")

# Graphique des soldes
st.subheader("Distribution des soldes")
st.bar_chart(df["solde"])

# Liste des clients à risque
st.subheader("Clients à risque")
st.dataframe(df[df["is_risky"] == True])

# Alerte si trop de risques
if df["is_risky"].mean() > 0.3:
    st.warning("Plus de 30% des clients sont à risque !")
