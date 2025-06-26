import streamlit as st
import pandas as pd
from io import BytesIO

# Configuración de la página
st.set_page_config(page_title="📦 Proveedores BSP", layout="wide")

st.title("📦 Visualizador: Proveedores BSP")
st.write("Visualiza, filtra y descarga la información desde el archivo Excel proporcionado.")

# Cargar archivo Excel automáticamente
nombre_archivo = "Proveedores_BSP.xlsx"

try:
    xls = pd.ExcelFile(nombre_archivo)
    hoja = st.selectbox("Selecciona una hoja:", xls.sheet_names)
    df = xls.parse(hoja)

    st.subheader(f"Vista previa: {hoja}")
    st.dataframe(df, use_container_width=True)

    st.markdown("### 🔍 Filtros")
    columna = st.selectbox("Columna para filtrar", df.columns)
    texto = st.text_input("Valor a buscar (contiene):")

    if texto:
        df_filtrado = df[df[columna].astype(str).str.contains(texto, case=False)]
        st.dataframe(df_filtrado, use_container_width=True)
    else:
        df_filtrado = df

    def to_excel(df_filtrado):
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df_filtrado.to_excel(writer, index=False, sheet_name="Filtrado")
        return output.getvalue()

    st.download_button(
        label="⬇️ Descargar tabla filtrada",
        data=to_excel(df_filtrado),
        file_name="tabla_filtrada_proveedores.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

except FileNotFoundError:
    st.error(f"No se encontró el archivo '{nombre_archivo}'. Asegúrate de que esté en la misma carpeta que este archivo app.py.")
