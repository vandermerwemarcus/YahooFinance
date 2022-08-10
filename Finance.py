#https://analyzingalpha.com/yfinance-python
import yfinance as yf
import streamlit as st
msft = yf.Ticker("CFR.JO")
info = msft.info
ROE = info['returnOnEquity']
PE = info['trailingPE']
K = info['payoutRatio']
RR = 1-K
g = 100*ROE*RR
PEG = PE/g
st.write('Trailing PE:',PE)
st.write('PEG:',PEG)
st.write('ROE:',ROE)
st.write('Payout ratio:',K)
st.write('Retention Rate:',RR)
st.write('Growth Rate:',g,'%')
st.write('Ticker:',info['symbol'])
st.write('Name:',info['shortName'])
st.write(info)
#st.write(info.keys())
