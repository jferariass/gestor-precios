import streamlit as st
import pandas as pd

st.title("🧂 Base de Datos de Ingredientes")

with st.form("nuevo_insumo"):
    nombre = st.text_input("Nombre (ej: Harina)")
    precio = st.number_input("Precio de compra ($)", min_value=0.0)
    cantidad = st.number_input("Cantidad total (g o ml)", min_value=1.0)
    if st.form_submit_button("Guardar"):
        costo_u = precio / cantidad
        st.session_state.ingredientes.append({
            "Nombre": nombre, "Precio": precio, "Cantidad": cantidad, "Costo Unit": costo_u
        })
        st.success("Guardado!")

if st.session_state.ingredientes:
    st.table(st.session_state.ingredientes)
