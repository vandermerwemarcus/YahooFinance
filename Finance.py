#https://analyzingalpha.com/yfinance-python
import yfinance as yf
import streamlit as st
import pandas as pd
matrix = pd.DataFrame(columns=[])
def sdata(tic):
  dic = dict();
  msft = yf.Ticker(tic)
  info = msft.info
  
  try:
    ROE = round(100*info['returnOnEquity'],2)
  except Exception:
    ROE = 0
    
  try:
    PE = round(info['trailingPE'],2)
  except Exception:
    PE = 0
  
  try:
    FPE = info['forwardEps']
  except Exception:
    FPE = 0
    
  try:
    K = round(info['payoutRatio'],2)
  except Exception:
    K = 0
  
  try:
    EPS = info['trailingEps']
  except Exception:
    EPS = 0
  
  try:
    LP = info['previousClose']/100
  except Exception:
    LP = 0
    
  try:
    EV = info['enterpriseToEbitda']
  except Exception:
    EV = 0
  
  try:
    ER = info['enterpriseToRevenue']
  except Exception:
    ER = 0
  
  RR = round(1-K,2)
  g = round(ROE*RR,2)
  
  try:
    PEG = round(PE/g,2)
  except ZeroDivisionError:
    PEG = 0
    
  PP = round(EPS * 20)

  #st.write('Name:',info['shortName'])
  #st.write('Ticker:',info['symbol'])
  #st.write('Last closing price:',LP)
  #st.write('Calculated Price:',PP)
  #st.write('EPS:',EPS)
  #st.write('Forward EPS',FPE)
  #st.write('ROE:',ROE,'%')
  #st.write('Trailing PE:',PE)
  #st.write('PEG:',PEG)
  #st.write('EV/EBITDA:',EV)
  #st.write('EV/Revenue:',ER)
  #st.write('Payout ratio:',K)
  #st.write('Retention Rate:',RR)
  #st.write('Growth Rate:',g,'%')
  #st.write(info)
  dic['PE'] = PE
  dic['LP'] = LP
  dic['ROE'] = ROE
  dic['Name'] = info['shortName']
  return dic
  #st.write(info.keys())

sdata('BVT.JO')

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
        'BVT.JO',
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
        'MRP.JO',
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
    f = sdata(i)
    st.write(f)
