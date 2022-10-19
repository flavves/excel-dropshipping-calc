# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:01:17 2022

@author: okmen
"""

import random
import pandas as pd



keyler=[]

for i in range(0,5000):
    keyler.append(random.randint(1234567891234567,9876543218749587))


keyler=list(set(keyler))


sonuc_df = pd.DataFrame(list(zip(keyler)),
                           columns =["keyler"])
print(sonuc_df)
            
sonuc_df.to_excel("keyler.xlsx",index=False)