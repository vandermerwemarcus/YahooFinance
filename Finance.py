#https://analyzingalpha.com/yfinance-python
import yfinance as yf
import streamlit as st
msft = yf.Ticker("CFR.JO")
info = msft.info
st.write('Trailing PE:',info['trailingPE'])
st.write('ROE:',info['returnOnEquity'])
st.write('ROE:',info['symbol'])
st.write(info)
#st.write(info.keys())
