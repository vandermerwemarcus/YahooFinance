import yfinance as yf
import streamlit as st
msft = yf.Ticker("CFR.JO")
info = msft.info
#st.write(info)
st.write(info['sector'])
st.write(info.keys())
