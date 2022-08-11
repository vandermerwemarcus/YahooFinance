#https://analyzingalpha.com/yfinance-python
import yfinance as yf
import streamlit as st
msft = yf.Ticker("SHP.JO")
info = msft.info
ROE = 100*info['returnOnEquity']
PE = round(info['trailingPE'],2)
K = round(info['payoutRatio'],2)
RR = 1-K
g = 100*ROE*RR
PEG = round(PE/g,2)
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
