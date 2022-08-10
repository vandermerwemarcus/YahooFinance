import yfinance as yf
import streamlit as st
msft = yf.Ticker("CFR.JO")
info = msft.info
st.write('Trailing PE:',info['trailingPE'])
st.write(info)
#st.write(info.keys())
