#https://analyzingalpha.com/yfinance-python
import yfinance as yf
import streamlit as st
msft = yf.Ticker("SHP.JO")
info = msft.info
ROE = info['returnOnEquity']
PE = round(info['trailingPE'],2)
K = info['payoutRatio']
RR = 1-K
g = 100*ROE*RR
PEG = PE/g
EPS = info['trailingEps']
#TPEG = info['trailingPegRatio']
st.write('Trailing PE:',PE)
st.write('PEG:',PEG)
#st.write('Trailing PEG:',TPEG)
st.write('EPS:',EPS)
st.write('ROE:',ROE)
st.write('Payout ratio:',K)
st.write('Retention Rate:',RR)
st.write('Growth Rate:',g,'%')
st.write('Ticker:',info['symbol'])
st.write('Name:',info['shortName'])
st.write(info)
#st.write(info.keys())
