#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:09:49 2017

@author: zzou
"""

from alpha_vantage.techindicators import TechIndicators
from urllib2 import HTTPError
import time
import numpy as np
from alpha_vantage.timeseries import TimeSeries

text_file = open("daily.sel", "r")
symbols = text_file.read().split()
bull_flag = []

ts = TimeSeries(key = 'MKAV2AXSQSPRE2R0',output_format = 'pandas')
for s in symbols:
    try:
        data, meta_data = ts.get_daily_adjusted(symbol = s)
        close_price = data["close"]
        for i in range(-10, -3):
            if (data["close"][i] >= 1.05 * data["open"][i]):
                bull_range = data["close"][i] - data["open"][i]
                current_position_since_bull = data["close"][-1] - data["open"][i]
                if (current_position_since_bull > 0.5 * bull_range):
                    bull_flag.append(s)
                    break
    except HTTPError:
        time.sleep(5)
        continue
 
output_file = open("bull_flag.sel", "a")
output_file.write("\n".join(bull_flag))
output_file.close()