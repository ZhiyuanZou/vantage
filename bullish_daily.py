#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:06:16 2017

@author: zzou
"""

from alpha_vantage.techindicators import TechIndicators
from urllib2 import HTTPError
import time
import numpy as np
from alpha_vantage.timeseries import TimeSeries

text_file = open("weekly.sel", "r")
symbols = text_file.read().split()
bullish_daily = []
cross_SMA = []

ts = TimeSeries(key = 'MKAV2AXSQSPRE2R0',output_format = 'pandas')
for s in symbols:
    try:
        data, meta_data = ts.get_daily_adjusted(symbol = s)
        close_price = data["close"]
        high5 = max(data["high"][-5:-1])
        low5 = min(data["low"][-5:-1])
        sma10 = np.mean(close_price[-10:-1])
        sma15 = np.mean(close_price[-15:-1])
        sma20 = np.mean(close_price[-20:-1])
        if (sma10 > sma15 and sma15 > sma20):
            bullish_daily.append(s)
            if (high5 >= sma10 and low5 <= sma20):
                cross_SMA.append(s)
    except HTTPError:
        time.sleep(5)
        continue
 
output_file = open("daily.sel", "w")
output_file.write("\n".join(bullish_daily))
cross_SMA_file = open("cross.sel", "w")
cross_SMA_file.write("\n".join(cross_SMA))
text_file.close()
output_file.close()
cross_SMA_file.close()