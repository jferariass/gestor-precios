import streamlit as st

st.set_page_config(page_title="Gestor de Precios", layout="wide")

st.title("💰 Sistema de Gestión de Costos")
st.write("Bienvenido. Selecciona una sección en el menú lateral para comenzar.")

# Inicializamos la memoria de la app para que no se borren los datos al navegar
if 'ingredientes' not in st.session_state:
    st.session_state.ingredientes = []
if 'recetas' not in st.session_state:
    st.session_state.recetas = []
