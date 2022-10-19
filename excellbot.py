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

katsayi=2.6
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
market_price = ticker.info['regularMarketPrice']





df = pd.read_excel('CA TO COM FİYAT HESAPLAMA DOSYASI.xlsx', sheet_name='Sayfa2')

# print whole sheet data
#print(df)
ilk_asin=df.columns[0]
ilk_fiyat=df.columns[1]
iki_asin=df.columns[2]
iki_fiyat=df.columns[3]

df[ilk_asin]
#df[df.duplicated([ilk_asin])]

df_com=df[ilk_asin],df[ilk_fiyat]

com_icin = pd.DataFrame()

com_icin[ilk_asin]=df[ilk_asin]
com_icin[ilk_fiyat]=df[ilk_fiyat]


cad_icin = pd.DataFrame()

cad_icin[iki_asin]=df[iki_asin]
cad_icin[iki_fiyat]=df[iki_fiyat]



com_asin_list=[]
com_fiyat_list=[]
ca_asin_list=[]
ca_fiyat_list=[]



for com_asini in com_icin[ilk_asin]:
    for cad_asini in cad_icin[iki_asin]:
        if com_asini == cad_asini:
            #print(com_asini)
            
            index_com=com_icin.loc[df[ilk_asin] == com_asini].index[0]
            index_cad=cad_icin.loc[df[iki_asin] == cad_asini].index[0]
            com_fiyati=df[ilk_fiyat][index_com]
            ca_fiyati=df[iki_fiyat][index_cad]
            islemsonucu=(ca_fiyati*market_price)/com_fiyati
            if islemsonucu>katsayi:
                
                com_asin_list.append(com_asini)
                com_fiyat_list.append(com_fiyati)
                ca_asin_list.append(cad_asini)
                ca_fiyat_list.append(ca_fiyati)
    
                
            break

sonuc_df = pd.DataFrame(list(zip(com_asin_list, com_fiyat_list,ca_asin_list,ca_fiyat_list)),
               columns =[ilk_asin, ilk_fiyat,iki_asin, iki_fiyat])
print(sonuc_df)

sonuc_df.to_excel("sonuc.xlsx",index=False)
txt=sonuc_df.to_string(index=False)

with open("sonuc.txt", "w") as dosya:
    dosya.write(txt)
















