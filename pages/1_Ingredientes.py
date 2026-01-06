import streamlit as st
import pandas as pd

st.title("🧂 Insumos e Ingredientes")

# CSS Local para esta página
st.markdown("""
    <style>
    .stDataFrame { border-radius: 20px; overflow: hidden; }
    </style>
    """, unsafe_allow_html=True)

with st.form("nuevo_ingrediente", clear_on_submit=True):
    st.markdown("### ➕ Registrar Compra")
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre del ingrediente")
        precio = st.number_input("Precio pagado ($)", min_value=0.0, step=0.01)
    with col2:
        cantidad = st.number_input("Cantidad neta (g/ml)", min_value=1.0, step=1.0)
        unidad = st.selectbox("Unidad", ["Gramos (g)", "Mililitros (ml)", "Unidades"])
    
    if st.form_submit_button("Guardar en Inventario"):
        if nombre:
            costo_u = precio / cantidad
            st.session_state.ingredientes.append({
                "Nombre": nombre, 
                "Precio": precio, 
                "Cantidad": cantidad, 
                "Costo Unit": round(costo_u, 4)
            })
            st.success(f"¡{nombre} añadido con éxito!")
        else:
            st.error("Falta el nombre.")

# Tabla de consulta con diseño
st.write("---")
st.subheader("📋 Lista de Precios Guardados")
if st.session_state.ingredientes:
    df = pd.DataFrame(st.session_state.ingredientes)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Aún no tienes ingredientes cargados.")
