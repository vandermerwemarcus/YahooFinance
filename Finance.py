#https://analyzingalpha.com/yfinance-python
import yfinance as yf
import streamlit as st
msft = yf.Ticker("CFR.JO")
info = msft.info
st.write('Trailing PE:',info['trailingPE'])
st.write('ROE:',info['returnOnEquity'])
st.write('Ticker:',info['symbol'])
st.write('Name:',info['shortName'])
st.write('Payout ratio:',info['payoutRatio'])
st.write(info)
#st.write(info.keys())
