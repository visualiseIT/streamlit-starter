import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Price App")

st.write("This app allows you to visualize your stock price.")

ticker = st.text_input("Enter a stock ticker:", "GOOG")
data = yf.download(ticker, start='2020-01-01', end='2021-01-01')
st.line_chart(data['Close'])
st.line_chart(data['Volume'])
