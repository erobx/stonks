'''
This is to test the yfinance module and see how it structures the data
'''
import pandas as pd
from yahoo_fin import stock_info as si
import csv
import numpy as np

'''Code from: https://levelup.gitconnected.com/how-to-get-all-stock-symbols-a73925c16a1b'''

# gather stock symbols from major US exchanges
df1 = pd.DataFrame(si.tickers_sp500())
df2 = pd.DataFrame(si.tickers_nasdaq())
df3 = pd.DataFrame(si.tickers_dow())
df4 = pd.DataFrame(si.tickers_other())

# convert DataFrame to list, then to sets
sym1 = set(symbol for symbol in df1[0].values.tolist())
sym2 = set(symbol for symbol in df2[0].values.tolist())
sym3 = set(symbol for symbol in df3[0].values.tolist())
sym4 = set(symbol for symbol in df4[0].values.tolist() if symbol != "")

# join the 4 sets into one. Because it's a set, there will be no duplicate symbols
symbols = set.union(sym1, sym2, sym3, sym4)

# Some stocks are 5 characters. Those stocks with the suffixes listed below are not of interest.
my_list = ['W', 'R', 'P', 'Q']
del_set = set()
sav_set = set()

for symbol in symbols:
    if len(symbol) > 4 and symbol[-1] in my_list:
        del_set.add(symbol)
    else:
        sav_set.add(symbol)

s = list(sav_set)
x = np.reshape(s, (len(s), 1))
header = ['ticker']

with open('tickers.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(x)

f.close()