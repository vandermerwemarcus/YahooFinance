import yfinance as yf
import streamlit as st
msft = yf.Ticker("CFR.JO")
info = msft.info
#st.write(info)
st.write(info['trailingPE'])
st.write(info.keys())
