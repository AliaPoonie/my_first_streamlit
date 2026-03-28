import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Étape 2 : Configuration de la page
# -------------------------------
st.set_page_config(
    page_title="Dashboard Ventes",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# -------------------------------
# Étape 3 : Menu multi-pages via la sidebar
# -------------------------------
page = st.sidebar.selectbox(
    "Navigation",
    ["Accueil", "Analyse", "Graphiques"]
)

# -------------------------------
# Étape 4 : Page Accueil
# -------------------------------
if page == "Accueil":
    # Titre principal
    st.title("Bienvenue sur le Dashboard")

    # Texte introductif
    st.write(
        "Ceci est la page d'accueil avec un résumé des informations principales."
    )

    # Lien vers la documentation officielle Streamlit
    st.markdown(
        "Pour en savoir plus sur Streamlit, visitez [la documentation](https://docs.streamlit.io/library)."
    )

    # Ajouter une image depuis une URL publique (version moderne)
    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png",
        caption="Logo Streamlit",
        use_container_width=True
    )

    # Ajouter un résumé ou indicateur simple
    st.metric(label="Nombre de visiteurs", value="1 234", delta="+12%")
    
    # Texte explicatif supplémentaire
    st.write(
        "Ce dashboard est conçu pour vous fournir une vue d'ensemble rapide de vos données et analyses."
    )

# -------------------------------
# Étape 5 : Page Analyse
# -------------------------------
elif page == "Analyse":
    st.title("Analyse des données")
    st.write("Cette page contient des tableaux et statistiques des ventes.")
    
    # Widgets interactifs
    option = st.selectbox(
        "Choisissez une catégorie",
        ["Catégorie A", "Catégorie B", "Catégorie C"]
    )
    valeur = st.slider(
        "Sélectionner une valeur", 0, 100, 50
    )
    
    st.write(f"Catégorie sélectionnée : {option}")
    st.write(f"Valeur choisie : {valeur}")

    # Sélecteurs de date
    st.date_input("Date de début")
    st.date_input("Date de fin")
    
    # Exemple de tableau
    data = pd.DataFrame({
        "Produit": ["Produit 1", "Produit 2", "Produit 3"],
        "Ventes": [100, 200, 150]
    })
    st.table(data)
    
    # Bouton pour télécharger le tableau
    st.download_button(
        label="Télécharger les données",
        data=data.to_csv(index=False).encode('utf-8'),
        file_name='ventes.csv',
        mime='text/csv'
    )

    # Lien vers la documentation
    st.link_button(
        "Voir la documentation du link_button",
        "https://docs.streamlit.io/develop/api-reference/widgets/st.link_button"
    )


# -------------------------------
# Étape 6 : Page Graphiques
# -------------------------------
elif page == "Graphiques":
    st.title("Visualisations interactives")
    
    # Dataset simulé
    df_data = pd.DataFrame({
        "Jour": ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"],
        "Ventes": [100, 150, 200, 170, 220],
        "Commandes": [15, 60, 10, 36, 87],
        "Clients": [5, 8, 12, 7, 10]
    })
    
    # Sélection de la variable à visualiser
    variable = st.selectbox(
        "Choisissez la variable à visualiser", 
        ["Ventes", "Commandes", "Clients"]
    )
    
    # Colonnes pour graphiques côte à côte
    col1, col2 = st.columns(2)
    
    # Graphique linéaire dynamique
    col1.header(f"Évolution de {variable}")
    col1.line_chart(df_data.set_index("Jour")[variable])
    
    # Graphique à barres dynamique
    col2.header(f"Répartition de {variable} par jour")
    col2.bar_chart(df_data.set_index("Jour")[variable])
    
    # Graphique Plotly interactif
    st.subheader(f"Scatter Plot interactif de {variable}")
    fig = px.scatter(
        df_data,
        x="Jour",
        y=variable,
        size=variable,
        color=variable,
        color_continuous_scale=px.colors.sequential.Viridis,
        size_max=50,
        title=f"Scatter Plot de {variable} par jour"
    )
    st.plotly_chart(fig)
    
    # Expander pour détails supplémentaires
    with st.expander("Détails supplémentaires"):
        st.write("Données complètes utilisées pour les visualisations :")
        st.dataframe(df_data)