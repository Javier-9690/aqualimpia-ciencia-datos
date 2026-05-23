import streamlit as st
import pandas as pd
import plotly.express as px

from src.funciones_aqualimpia import cargar_datos, preparar_datos, resumen_por_planta

st.set_page_config(page_title="Dashboard AquaLimpia", layout="wide")

st.title("Dashboard exploratorio - AquaLimpia S. A.")

df = cargar_datos("data/raw/dataset_set_A_aguas_residuales.xlsx")
df = preparar_datos(df)

planta = st.sidebar.multiselect(
    "Seleccionar planta",
    options=df["planta"].unique(),
    default=df["planta"].unique()
)

df_filtrado = df[df["planta"].isin(planta)]

cumplimiento = df_filtrado["cumplimiento_norma"].mean() * 100
dbo_promedio = df_filtrado["DBO_salida_mg_L"].mean()
eficiencia = df_filtrado["eficiencia_DBO_pct"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Cumplimiento normativo", f"{cumplimiento:.1f}%")
col2.metric("DBO salida promedio", f"{dbo_promedio:.2f} mg/L")
col3.metric("Eficiencia DBO promedio", f"{eficiencia:.2f}%")

resumen = resumen_por_planta(df_filtrado)

fig1 = px.bar(
    resumen,
    x="planta",
    y="cumplimiento_pct",
    title="Cumplimiento promedio por planta"
)

fig2 = px.box(
    df_filtrado,
    x="planta",
    y="DBO_salida_mg_L",
    title="Distribución de DBO de salida por planta"
)

fig3 = px.scatter(
    df_filtrado,
    x="DBO_entrada_mg_L",
    y="DBO_salida_mg_L",
    color="planta",
    title="Relación entre DBO de entrada y DBO de salida"
)

fig4 = px.line(
    df_filtrado.sort_values("fecha_registro"),
    x="fecha_registro",
    y="DBO_salida_mg_L",
    color="planta",
    title="Evolución temporal de DBO de salida"
)

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Registros con alerta operativa")
st.dataframe(df_filtrado[df_filtrado["alerta_operativa"] == "Alerta"])