from alpha_vantage.techindicators import TechIndicators
from urllib2 import HTTPError
import time

text_file = open("symbols.txt", "r")
symbols = text_file.read().split()
bullish_weekly = []
ti = TechIndicators(key = 'MKAV2AXSQSPRE2R0',output_format = 'pandas')
for s in symbols:
    try:
        data, meta_data = ti.get_sma(symbol = s, interval = 'weekly', time_period = 10, series_type = 'close')
        sma10 = data['SMA'][-1]
        data, meta_data = ti.get_sma(symbol = s, interval = 'weekly', time_period = 15, series_type = 'close')
        sma15 = data['SMA'][-1]
        data, meta_data = ti.get_sma(symbol = s, interval = 'weekly', time_period = 20, series_type = 'close')
        sma20 = data['SMA'][-1]
        if (sma10 > sma15 and sma15 > sma20):
            bullish_weekly.append(s)
    except HTTPError:
        time.sleep(30)
output_file = open("output.sel", "w")
output_file.write("\n".join(bullish_weekly))
text_file.close()
output_file.close()

