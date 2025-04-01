import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" 
         
### Resumo do Mercado de Ações APPLE 
         
#### Indicadores Preço x Volume: Março/2024 - Março/2025


""")

# simbolo ações da Apple
Simbolo_Ticker = 'AAPL'
# obtém os dados das ações da Apple
Data_Ticker = yf.Ticker(Simbolo_Ticker)
# define histórico de preços das ações
Dataframe_Ticker = Data_Ticker.history(period='1d', start='2024-2-29', end='2025-3-30')

st.write("""
    ## Cotação de fechamento
""")

st.line_chart(Dataframe_Ticker.Close)

st.write("""
    ## Volume Financeiro
""")

st.bar_chart(Dataframe_Ticker.Volume)





