import yahoo_fin.stock_info as si
import pandas as pd
import sqlite3
import yfinance as yf
# 1
yf_header = 'logo_url'
# 5
si_quote_headers = [
            'PE Ratio (TTM)', 'Avg. Volume', 'Previous Close',
            'Market Cap', 'EPS (TTM)']
# 2
si_info_headers = ['sector', 'fullTimeEmployees']
# 3
si_stats_headers = ['Revenue (ttm)', 'Quarterly Revenue Growth', 'Gross Profit (ttm)']

ticker = "ATCX"

logo = yf.Ticker(ticker).info[yf_header]
quote_table = si.get_quote_table(ticker)
info = si.get_company_info(ticker)
stats = si.get_stats(ticker)

result = [logo]
quotes = [quote_table[h] for h in si_quote_headers]
for i in quotes:
    result.append(i)

for h in si_info_headers:
    value = info['Value'][h]
    if value != '':
        result.append(value)
    else:
        result.append('nan')

for h in si_stats_headers:
    value = stats[stats['Attribute']==h]
    if not value.empty:
        value = value.iloc[0]['Value']
        result.append(value)
    else:
        result.append('nan')

print(result)

#conn = sqlite3.connect('instance/stonks.sqlite')
#pd.DataFrame.to_sql('test.sql', conn, msft)