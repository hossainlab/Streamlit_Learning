import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Stock App
Shown the stock **closing** price and **volume** of Google!
""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period=id, start='2010-05-31', end='2020-05-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
