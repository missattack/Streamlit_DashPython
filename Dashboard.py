import streamlit as st
import yfinance as fy
import pandas as pd

st.title('Gráfico Financeiro - Setor de Consumo e Varejo Brasileiro')

st.write("""
#### Empresas: Ambev, Magazine Luiza, Via (Casas Bahia), Assaí Atacadista e Carrefour Brasil 
""")

tickers = ('ABEV3.SA','MGLU3.SA','VIIA3.SA','ASAI3.SA','CRFB3.SA')


drop_selecao = st.multiselect('Selecione o ativo (tickers)', tickers)

dt_inicio = st.date_input('Início', value = pd.to_datetime('2020-01-01'), format='DD/MM/YYYY')
dt_fim = st.date_input('Fim', value = pd.to_datetime('today'), format='DD/MM/YYYY')

def compare(df):
    # calcula a variação percentual entre o elemento atual e o anterior
    rel = df.pct_change()
    # calcula o produto acumulado de uma série de valores cumprod()
    acum = (1+rel).cumprod() - 1
    acum = acum.fillna(0)   # preenche nulo com 0
    return acum

if len(drop_selecao) > 0:
    df = compare(fy.download(drop_selecao, dt_inicio, dt_fim)['Close'])
    st.header('Retorno dos Ativos {}'.format(drop_selecao))
    st.line_chart(df)