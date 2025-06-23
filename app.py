
import streamlit as st
import pandas as pd
from datetime import datetime

MILHEIRO = {
    "LATAM": 0.029,
    "GOL": 0.021,
    "AZUL": 0.022,
    "TAP": 0.053
}

def calcular_orcamento(tipo_passagem, companhia, milhas_ida, milhas_volta,
                       taxa_embarque_ida, taxa_embarque_volta, bagagem_total, passageiros):
    custo_milha = MILHEIRO.get(companhia.upper(), 0)
    valor_milhas = (milhas_ida + milhas_volta) * custo_milha
    taxas = taxa_embarque_ida + taxa_embarque_volta
    total_base = valor_milhas + taxas
    acrescimo = 1.07 if tipo_passagem == "TCM" else 1.10
    total_com_acrescimo = total_base * acrescimo
    total_final = (total_com_acrescimo + bagagem_total) * passageiros
    return round(total_final, 2)

st.set_page_config(page_title="Orçamento 2A Milhas", layout="centered")
st.title("Sistema de Orçamento - 2A Milhas")

st.header("Dados do agente e cliente")
nome_agente = st.text_input("Nome do agente")
nome_cliente = st.text_input("Nome do cliente")

st.header("Dados da viagem")
col1, col2 = st.columns(2)
with col1:
    origem = st.text_input("Local de origem")
    data_ida = st.date_input("Data de origem")
    malas_ida = st.number_input("Malas despachadas (ida)", min_value=0, step=1)
with col2:
    destino = st.text_input("Local de destino")
    data_volta = st.date_input("Data de destino")
    malas_volta = st.number_input("Malas despachadas (volta)", min_value=0, step=1)

st.header("Dados da cotação")
companhia = st.selectbox("Companhia aérea", list(MILHEIRO.keys()))
tipo_passagem = st.radio("Tipo de passagem", ["TSM", "TCM"])

milhas_ida = st.number_input("Milhas na ida", min_value=0)
milhas_volta = st.number_input("Milhas na volta", min_value=0)
taxa_embarque_ida = st.number_input("Taxa de embarque ida (R$)", min_value=0.0)
taxa_embarque_volta = st.number_input("Taxa de embarque volta (R$)", min_value=0.0)
bagagem_total = st.number_input("Valor total das bagagens (R$)", min_value=0.0)
passageiros = st.number_input("Número de passageiros", min_value=1, step=1)

if st.button("Calcular orçamento"):
    total = calcular_orcamento(tipo_passagem, companhia, milhas_ida, milhas_volta,
                               taxa_embarque_ida, taxa_embarque_volta, bagagem_total, passageiros)
    st.success(f"Orçamento total para o cliente {nome_cliente}: R$ {total:,.2f}")
