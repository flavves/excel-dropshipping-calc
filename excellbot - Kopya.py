# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:27:55 2022

@author: okmen
"""

import pandas as pd
import yfinance as yf
"""

Canada CAD=X
Meksika MXN=X
Birleşik Arap emirlikleri AED
Singapur SGD 
Avustralya AUD
Japonya JPY
Almanya EUR
Brezilya BRL
Fransa EUR
Hollanda EUR

"""

katsayi=2.4
ulke="Singapur"

if ulke=="Kanada":
    parabirimi="CAD=X"
elif ulke=="Meksika":
    parabirimi="MXN=X"
elif ulke=="Birleşik Arap emirlikleri":
    parabirimi="AED=X"
elif ulke=="Singapur":
    parabirimi="SGD=X"
elif ulke=="Japonya":
    parabirimi="JPY=X"
elif ulke=="Avustralya":
    parabirimi="AUD=X"
elif ulke=="Almanya":
    parabirimi="EUR=X"
elif ulke=="Brezilya":
    parabirimi="BRL=X"
elif ulke=="Fransa":
    parabirimi="EUR=X"
elif ulke=="Hollanda":
    parabirimi="EUR=X"

ticker = yf.Ticker(parabirimi)
ticker.info
market_price = ticker.info['regularMarketPrice']





df = pd.read_excel('CA TO COM FİYAT HESAPLAMA DOSYASI.xlsx', sheet_name='Sayfa2')

# print whole sheet data
print(df)
df.columns[0]

df["com asin"]
#df[df.duplicated(['com asin'])]

df_com=df["com asin"],df["com fiyat"]

com_icin = pd.DataFrame()

com_icin["com asin"]=df["com asin"]
com_icin["com fiyat"]=df["com fiyat"]


cad_icin = pd.DataFrame()

cad_icin["ca asin"]=df["ca asin"]
cad_icin["ca fiyat"]=df["ca fiyat"]



com_asin_list=[]
com_fiyat_list=[]
ca_asin_list=[]
ca_fiyat_list=[]



for com_asini in com_icin["com asin"]:
    for cad_asini in cad_icin["ca asin"]:
        if com_asini == cad_asini:
            print(com_asini)
            
            index_com=com_icin.loc[df['com asin'] == com_asini].index[0]
            index_cad=cad_icin.loc[df['ca asin'] == cad_asini].index[0]
            com_fiyati=df['com fiyat'][index_com]
            ca_fiyati=df['ca fiyat'][index_cad]
            islemsonucu=(ca_fiyati*market_price)/com_fiyati
            if islemsonucu>katsayi:
                
                com_asin_list.append(com_asini)
                com_fiyat_list.append(com_fiyati)
                ca_asin_list.append(cad_asini)
                ca_fiyat_list.append(ca_fiyati)
    
                
            break

sonuc_df = pd.DataFrame(list(zip(com_asin_list, com_fiyat_list,ca_asin_list,ca_fiyat_list)),
               columns =['com asin', 'com fiyat','ca asin', 'ca fiyat'])
print(sonuc_df)




