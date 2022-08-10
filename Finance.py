import yfinance as yf
import streamlit as st
msft = yf.Ticker("CFR.JO")
st.write(msft.info.zip)
