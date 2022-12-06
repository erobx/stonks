import yahoo_fin.stock_info as si
import pandas as pd
import sqlite3
import yfinance as yf
import csv
import numpy as np

# 1
yf_header = ['logo_url']
# 5
si_quote_headers = [
            'PE Ratio (TTM)', 'Avg. Volume', 'Previous Close',
            'Market Cap', 'EPS (TTM)']
# 2
si_info_headers = ['sector', 'fullTimeEmployees']
# 3
si_stats_headers = ['Revenue (ttm)', 'Quarterly Revenue Growth', 'Gross Profit (ttm)']

headers = yf_header + si_quote_headers + si_info_headers + si_stats_headers

tickers = ['MSFT', 'TSLA', 'FTNT', 'ATCX']

rows = []

for t in tickers:
    logo = yf.Ticker(t).info[yf_header[0]]
    quote_table = si.get_quote_table(t)
    info = si.get_company_info(t)
    stats = si.get_stats(t)

    values = [logo]
    quotes = [quote_table[h] for h in si_quote_headers]
    for i in quotes:
        values.append(i)

    for h in si_info_headers:
        value = info['Value'][h]
        if value != '':
            values.append(value)
        else:
            values.append('nan')

    for h in si_stats_headers:
        value = stats[stats['Attribute']==h]
        if not value.empty:
            value = value.iloc[0]['Value']
            values.append(value)
        else:
            values.append('nan')

    rows.append(values)

rows = np.asarray(rows)
rows = np.reshape(rows, (len(rows), len(headers)))

with open('test.csv', 'w+', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

#conn = sqlite3.connect('instance/stonks.sqlite')
#pd.DataFrame.to_sql('test.sql', conn, msft)