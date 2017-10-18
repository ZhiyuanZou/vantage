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
#ti = TechIndicators(key = 'MKAV2AXSQSPRE2R0',output_format = 'pandas')
#for s in symbols:
#    try:
#        data, meta_data = ti.get_sma(symbol = s, interval = 'weekly', time_period = 10, series_type = 'close')
#        sma10 = data['SMA'][-1]
#        data, meta_data = ti.get_sma(symbol = s, interval = 'weekly', time_period = 15, series_type = 'close')
#        sma15 = data['SMA'][-1]
#        data, meta_data = ti.get_sma(symbol = s, interval = 'weekly', time_period = 20, series_type = 'close')
#        sma20 = data['SMA'][-1]
#        if (sma10 > sma15 and sma15 > sma20):
#            bullish_weekly.append(s)
#    except HTTPError:
#        time.sleep(30)

ts = TimeSeries(key = 'MKAV2AXSQSPRE2R0',output_format = 'pandas')
for s in symbols:
    try:
        data, meta_data = ts.(symbol = s)
        close_price = data["close"]
        sma10 = np.mean(close_price[-10:-1])
        sma15 = np.mean(close_price[-15:-1])
        sma20 = np.mean(close_price[-20:-1])
        if (sma10 > sma15 and sma15 > sma20):
            bullish_daily.append(s)
    except HTTPError:
        time.sleep(5)
        continue
 
output_file = open("daily.sel", "w")
output_file.write("\n".join(bullish_weekly))
text_file.close()
output_file.close()