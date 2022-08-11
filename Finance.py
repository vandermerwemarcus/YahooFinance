#https://analyzingalpha.com/yfinance-python
import yfinance as yf
import streamlit as st
msft = yf.Ticker("SOL.JO")
info = msft.info
ROE = round(100*info['returnOnEquity'],2)
PE = round(info['trailingPE'],2)
K = round(info['payoutRatio'],2)
RR = round(1-K,2)
g = round(ROE*RR,2)
PEG = round(PE/g,2)
EPS = info['trailingEps']
#TPEG = info['trailingPegRatio']
st.write('Trailing PE:',PE)
st.write('PEG:',PEG)
#st.write('Trailing PEG:',TPEG)
st.write('EPS:',EPS)
st.write('ROE:',ROE,'%')
st.write('Payout ratio:',K)
st.write('Retention Rate:',RR)
st.write('Growth Rate:',g,'%')
st.write('Ticker:',info['symbol'])
st.write('Name:',info['shortName'])
st.write(info)
#st.write(info.keys())
