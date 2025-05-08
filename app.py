import streamlit as st
from src.data_loader import load_data
from src.analyzer import calcular_kpis
from src.visualizer import gerar_mapa
import streamlit.components.v1 as components

st.title("GeoFiber - Monitoramento de Fibra Óptica")

df = load_data("data/sample_incidents.csv")

if df.empty:
    st.error("Erro ao carregar dados.")
else:
    kpis = calcular_kpis(df)
    st.metric("Total de Incidentes", kpis['total'])
    st.metric("Resolvidos", kpis['resolvidos'])
    st.metric("Pendentes", kpis['pendentes'])
    st.metric("Tempo Médio de Reparo (min)", round(kpis['tempo_medio_reparo'], 2))

    mapa = gerar_mapa(df)
    components.html(mapa._repr_html_(), height=500)