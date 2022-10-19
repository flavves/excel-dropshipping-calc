# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:55:09 2022

@author: okmen
"""

import yfinance as yf

ticker = yf.Ticker("MXN=X")
ticker.info
market_price = ticker.info['regularMarketPrice']
