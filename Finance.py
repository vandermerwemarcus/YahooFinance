#https://analyzingalpha.com/yfinance-python
import yfinance as yf
import streamlit as st

def sdata(tic):
  msft = yf.Ticker(tic)
  info = msft.info
  ROE = round(100*info['returnOnEquity'],2)
  PE = round(info['trailingPE'],2)
  K = round(info['payoutRatio'],2)
  RR = round(1-K,2)
  g = round(ROE*RR,2)
  PEG = round(PE/g,2)
  EPS = info['trailingEps']
  PP = EPS * 16
  LP = info['previousClose']
  st.write('Ticker:',info['symbol'])
  st.write('Name:',info['shortName'])
  st.write('Trailing PE:',PE)
  st.write('PEG:',PEG)
  st.write('Last closing price:',LP)
  st.write('Calculated Price:',PP)
  st.write('EPS:',EPS)
  st.write('ROE:',ROE,'%')
  st.write('Payout ratio:',K)
  st.write('Retention Rate:',RR)
  st.write('Growth Rate:',g,'%')
  st.write(info)
  #st.write(info.keys())

sdata('KIO.JO')
'''
stocks=['ANG.JO',
        'ACL.JO',
        'AEG.JO',
        'AFE.JO',
        'AGL.JO',
        'AMS.JO',
        'APN.JO',
        'ARI.JO',
        'ARL.JO',
        'BAW.JO',
        'BAT.JO',
        'CFR.JO',
        'CML.JO',
        'CPI.JO',
        'DRD.JO',
        'DSY.JO',
        'EOH.JO',
        'EXX.JO',
        'FSR.JO',
        'GFI.JO',
        'GLD.JO',
        'GLN.JO',
        'GND.JO',
        'HAR.JO',
        'IMP.JO',
        'JBL.JO',
        'KIO.JO',
        'MNP.JO',
        'MRF.JO',
        'MSM.JO',
        'MTN.JO',
        'NED.JO',
        'NPK.JO',
        'NPN.JO',
        'NTC.JO',
        'OMU.JO',
        'ORN.JO',
        'PAN.JO',
        'PIK.JO',
        'PPC.JO',
        'PPE.JO',
        'RDF.JO',
        'REM.JO',
        'REN.JO',
        'SBK.JO',
        'SHP.JO',
        'SLM.JO',
        'SOL.JO',
        'SUI.JO',
        'TBS.JO',
        'TGA.JO',
        'TKG.JO',
        'TRU.JO',
        'WHL.JO',]

for i in stocks:
    sdata(i)
'''
