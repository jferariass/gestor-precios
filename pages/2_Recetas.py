import streamlit as st
import pandas as pd

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Recetas", layout="centered")

# --- ARREGLO PARA EL ERROR (Inicialización) ---
if 'ingredientes' not in st.session_state:
    st.session_state.ingredientes = []
if 'receta_actual' not in st.session_state:
    st.session_state.receta_actual = []

st.title("🥣 Elaboración de Productos")

# ESTILO MODERNO
st.markdown("""
    <style>
    .stButton>button { border-radius: 15px !important; }
    .receta-card {
        background-color: #2c2c2e;
        padding: 15px;
        border-radius: 20px;
        margin-bottom: 10px;
        border-left: 5px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# LÓGICA DE LA PÁGINA
if not st.session_state.ingredientes:
    st.info("⚠️ Para empezar, primero carga tus ingredientes en la sección lateral 'Ingredientes'.")
else:
    with st.container():
        nombre_prod = st.text_input("Nombre del producto final", placeholder="Ej: Pizza especial")
        
        # Selector de ingredientes
        df_ing = pd.DataFrame(st.session_state.ingredientes)
        ing_seleccionado = st.selectbox("Elegir insumo", df_ing['Nombre'].unique())
        
        c1, c2 = st.columns([2, 1])
        with c1:
            cantidad = st.number_input("Cantidad (g/ml/unid)", min_value=0.0)
        with c2:
            st.write(" ") # Espaciador
            if st.button("➕ Añadir"):
                # Buscar costo unitario
                costo_u = df_ing.loc[df_ing['Nombre'] == ing_seleccionado, 'Costo Unit'].values[0]
                subtotal = costo_u * cantidad
                st.session_state.receta_actual.append({
                    "Ingrediente": ing_seleccionado,
                    "Cantidad": cantidad,
                    "Subtotal": round(subtotal, 2)
                })

    # Mostrar lo que vamos sumando
    if st.session_state.receta_actual:
        st.write("---")
        total_receta = 0
        for i, item in enumerate(st.session_state.receta_actual):
            st.markdown(f"""
                <div class="receta-card">
                    <b>{item['Ingrediente']}</b>: {item['Cantidad']} → ${item['Subtotal']}
                </div>
            """, unsafe_allow_html=True)
            total_costo = item['Subtotal']
            total_receta += total_costo
            
        st.markdown(f"### Costo Total: ${round(total_receta, 2)}")
        
        if st.button("🗑️ Limpiar todo"):
            st.session_state.receta_actual = []
            st.rerun()
