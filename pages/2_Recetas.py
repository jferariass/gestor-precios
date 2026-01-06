import streamlit as st
import pandas as pd

st.title("🥣 Elaboración de Productos")

# Estilo para mantener la estética redondeada
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] { border-radius: 12px !important; }
    .receta-card {
        background-color: #2c2c2e;
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 15px;
        border-left: 5px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

if not st.session_state.ingredientes:
    st.warning("⚠️ Primero carga ingredientes en la sección anterior para poder armar una receta.")
else:
    # 1. Datos del Producto
    with st.container():
        st.markdown("### 🏷️ Nuevo Producto")
        nombre_prod = st.text_input("Nombre del producto (ej: Tarta de Manzana)")
        
        # 2. Selección de Ingredientes
        st.write("---")
        st.markdown("#### Selecciona los componentes:")
        
        df_ing = pd.DataFrame(st.session_state.ingredientes)
        ingrediente_nombre = st.selectbox("Elegir insumo", df_ing['Nombre'].unique())
        
        col_cant, col_btn = st.columns([2, 1])
        with col_cant:
            cantidad_receta = st.number_input("Cantidad a usar (g/ml/unid)", min_value=0.0)
        
        # Inicializamos una lista temporal para la receta que estamos armando
        if 'receta_actual' not in st.session_state:
            st.session_state.receta_actual = []

        with col_btn:
            st.write(" ") # Espaciador
            if st.button("➕ Añadir"):
                # Buscamos el costo unitario del ingrediente elegido
                costo_u = df_ing.loc[df_ing['Nombre'] == ingrediente_nombre, 'Costo Unit'].values[0]
                subtotal = costo_u * cantidad_receta
                st.session_state.receta_actual.append({
                    "Ingrediente": ingrediente_nombre,
                    "Cantidad": cantidad_receta,
                    "Subtotal": round(subtotal, 2)
                })

    # 3. Resumen de la receta actual
    if st.session_state.receta_actual:
        st.write("---")
        st.subheader(f"Resumen para: {nombre_prod}")
        
        total_costo = 0
        for item in st.session_state.receta_actual:
            with st.container():
                st.markdown(f"""
                <div class="receta-card">
                    <strong>{item['Ingrediente']}</strong><br>
                    {item['Cantidad']} unidades/g/ml → <b>${item['Subtotal']}</b>
                </div>
                """, unsafe_allow_html=True)
                total_costo += item['Subtotal']
        
        st.markdown(f"## Costo Total de Producción: ${round(total_costo, 2)}")
        
        if st.button("🗑️ Limpiar Receta"):
            st.session_state.receta_actual = []
            st.rerun()
