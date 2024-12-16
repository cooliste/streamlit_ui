import streamlit as st
import pandas as pd
import plotly.express as px

# Chargement des données Iris
df = pd.read_csv("iris.csv")

# Titre de l'application
st.title("Blog d'Étude des Fleurs Iris 🌸")

# Sous-titre
st.subheader("Découvrez les caractéristiques des fleurs du célèbre dataset Iris")

# Description du dataset
st.markdown(
    """
    Le dataset **Iris** contient des mesures sur trois espèces de fleurs : *Setosa*, 
    *Versicolor*, et *Virginica*. Ce blog explore leurs caractéristiques, leurs atouts, 
    et leurs inconvénients, à l'aide de visualisations interactives.
    """
)

# Afficher les premières lignes du dataset
st.write("### Aperçu du Dataset")
st.dataframe(df.head())

# Graphique en ligne des mesures
st.write("### Variations des dimensions des fleurs")
feature = st.selectbox("Choisissez une caractéristique :", df.columns[:-1])  # Colonnes sauf la dernière

# Utilisation de Plotly pour le graphique en ligne
fig_line = px.line(df, x=df.index, y=feature, title=f'Variations de {feature}', labels={'x': 'Index', feature: feature})
st.plotly_chart(fig_line)

# Histogramme des dimensions avec Plotly
st.write("### Distribution des dimensions des fleurs")
fig_hist = px.histogram(df, x=feature, color="species", title=f'Distribution de {feature}', 
                         labels={feature: feature}, barmode='overlay', 
                         color_discrete_sequence=["#b56576", "#6d597a", "#355070"])
st.plotly_chart(fig_hist)

# Afficher les statistiques descriptives
st.write("### Statistiques descriptives")
st.write(df.describe())

# Section FAQ ou blog
st.write("### Blog sur les Fleurs Iris")
st.markdown(
    """
    - **Setosa** : Idéal pour les amateurs de fleurs compactes. 🌿  
      - *Atouts* : Taille petite, facile à cultiver.
      - *Inconvénients* : Moins impressionnante visuellement.
    - **Versicolor** : Un mélange parfait entre taille et élégance. 🌼  
      - *Atouts* : Taille moyenne, couleurs variées.
      - *Inconvénients* : Demande plus de soins.
    - **Virginica** : La plus grande et impressionnante des trois. 🌷  
      - *Atouts* : Grande taille, magnifique pour les jardins.
      - *Inconvénients* : Demande de l'espace.
    """
)