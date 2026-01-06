import streamlit as st

# Configuración de página con diseño centrado
st.set_page_config(page_title="Gestor Pro", layout="centered")

# --- DISEÑO GLOBAL MODERNO ---
st.markdown("""
    <style>
    /* Bordes redondeados para todos los contenedores */
    div[data-testid="stExpander"], div[data-testid="stForm"] {
        border-radius: 20px !important;
        border: 1px solid #333 !important;
        background-color: #1c1c1e !important;
        padding: 20px;
    }
    /* Estilo de los inputs */
    input { border-radius: 10px !important; }
    /* Estilo de botones */
    .stButton>button {
        border-radius: 12px !important;
        height: 3em !important;
        background: linear-gradient(145deg, #ff4b4b, #ff7575) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3) !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Panel de Control")
st.write("---")
st.info("Utiliza el menú lateral para gestionar tus ingredientes y recetas.")
