import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Titre de l'application
st.set_page_config(page_title="Analyse des Fleurs - Dataset Iris", layout="wide")
st.title("🌸 Analyse des Fleurs - Dataset Iris 🌸")

# Chargement des données
df = pd.read_csv("https://gist.github.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")
print(df.columns)
# Affichage d'un message d'accueil
st.write("Bienvenue sur notre site d'analyse des fleurs !")
st.write("Ce site utilise le dataset Iris pour explorer les caractéristiques des fleurs.")

# Affichage des données
st.subheader("Données sur les Fleurs")
st.dataframe(df)

# Visualisation des caractéristiques
st.subheader("Visualisation des Caractéristiques des Fleurs")

# Histogramme de la longueur des sépales
fig1 = px.histogram(df, x='sepal_length', color='variety', 
                     title='Distribution de la Longueur des Sépales',
                     labels={'sepal_length': 'Longueur des Sépales'},
                     color_discrete_sequence=px.colors.qualitative.Set1)

st.plotly_chart(fig1)

# Diagramme en boîte pour la largeur des sépales par espèce
fig2 = px.box(df, x='species', y='sepal_width', 
               title='Largeur des Sépales par Espèce',
               labels={'species': 'Espèce', 'sepal_width': 'Largeur des Sépales'},
               color='species',
               color_discrete_sequence=px.colors.qualitative.Set2)

st.plotly_chart(fig2)

# Visualisation de la relation entre longueur et largeur des sépales
fig3 = px.scatter(df, x='sepal_length', y='sepal_width', color='species',
                   title='Relation entre Longueur et Largeur des Sépales',
                   labels={'sepal_length': 'Longueur des Sépales', 'sepal_width': 'Largeur des Sépales'},
                   hover_data=['petal_length', 'petal_width'])

st.plotly_chart(fig3)

# Atouts et Désavantages
st.subheader("Atouts et Désavantages des Fleurs")
atouts = """
- Les fleurs du dataset Iris sont souvent utilisées pour l'enseignement de la classification.
- Elles présentent une belle diversité entre les espèces.
- Les caractéristiques mesurées (longueur et largeur des sépales et pétales) sont faciles à visualiser.
"""
desavantages = """
- Le dataset est relativement petit, ce qui peut ne pas représenter la complexité du monde réel.
- Les espèces peuvent ne pas être facilement distinguables dans certaines conditions.
"""

st.markdown("### Atouts")
st.write(atouts)
st.markdown("### Désavantages")
st.write(desavantages)

# Footer avec animation simple
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Créé avec ❤️ par [Ziyade CHABI MACO]</h5>", unsafe_allow_html=True)