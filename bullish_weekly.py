from alpha_vantage.techindicators import TechIndicators
from urllib2 import HTTPError
import time
import numpy as np
from alpha_vantage.timeseries import TimeSeries

text_file = open("symbols.txt", "r")
symbols = text_file.read().split()
bullish_weekly = []
weekly_cross = []
unprocessed = []
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
        data, meta_data = ts.get_weekly(symbol = s)
        close_price = data["close"]
        high5 = max(data["high"][-5:-1])
        low5 = min(data["low"][-5:-1])
        sma10 = np.mean(close_price[-10:-1])
        sma15 = np.mean(close_price[-15:-1])
        sma20 = np.mean(close_price[-20:-1])
        if (sma10 > sma15 and sma15 > sma20):
            bullish_weekly.append(s)
            if (high5 >= sma10 and low5 <= sma20):
                weekly_cross.append(s)
    except:
        print "Unexpected error:", s
        unprocessed.append(s)
        continue
 
output_file = open("weekly.txt", "w")
output_file.write("\n".join(bullish_weekly))
output_file.close()

output_file = open("unprocessed.txt", "w")
output_file.write("\n".join(unprocessed))
output_file.close()

cross_SMA_file = open("weekly_cross.txt", "w")
cross_SMA_file.write("\n".join(weekly_cross))
cross_SMA_file.close()

text_file.close()

