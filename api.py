'''
This is to test the yfinance module and see how it structures the data
'''
import warnings
warnings. simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from yahoo_fin import stock_info as si
import csv
import numpy as np
import yfinance as yf
import sqlite3

'''Code from: https://levelup.gitconnected.com/how-to-get-all-stock-symbols-a73925c16a1b'''
def get_stocks():
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
    
    return list(sav_set)

tickers = get_stocks()

def write_csv(n):
    # 1
    yf_header = ['logo_url', 'ticker']
    # 5
    si_quote_headers = [
                'PE Ratio (TTM)', 'Avg. Volume', 'Previous Close',
                'Market Cap', 'EPS (TTM)']
    # 2
    si_info_headers = ['sector', 'fullTimeEmployees']
    # 3
    si_stats_headers = ['Revenue (ttm)', 'Quarterly Revenue Growth (yoy)', 'Gross Profit (ttm)']

    headers = yf_header + si_quote_headers + si_info_headers + si_stats_headers

    rows = []
    counter = 0
    for t in tickers[:n]:
        if (t.find('$') != -1):
            continue
        elif (t.find('.') != -1):
            continue
        elif (len(t) > 4):
            continue

        print(t, ' ', counter)
        logo = yf.Ticker(t).info.get(yf_header[0])
        
        try:
            info = si.get_company_info(t)
        except TypeError:
            print('Could not get info')
            continue
        except KeyError:
            print('KeyError')
            continue

        try:
            quote_table = si.get_quote_table(t)
        except TypeError:
            print('Could not get quote table')
            continue
        except KeyError:
            print('KeyError')
            continue

        try:
            stats = si.get_stats(t)
        except TypeError:
            print('Could not get stats')
            continue
        except KeyError:
            print('KeyError')
            continue

        counter += 1
        if logo == '':
            values = ['nan', t]
        else:
            values = [logo, t]
        
        for h in si_quote_headers:
            value = quote_table.get(h)  
            if value != None:
                values.append(value)
            else:
                values.append('0')

        for h in si_info_headers:
            value = info['Value'].get(h)
            if value != None:
                values.append(value)
            else:
                values.append('Other')

        for h in si_stats_headers:
            value = stats[stats['Attribute']==h].reset_index()
            if not value.empty:
                value = value.iloc[0]['Value']
                values.append(value)
            else:
                values.append('nan')

        rows.append(values)

    rows = np.asarray(rows)
    rows = np.reshape(rows, (len(rows), len(headers)))

    with open('tickers.csv', 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    f.close()

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        file = open('tickers.csv')
        contents = csv.reader(file)
        insert_records = "INSERT INTO stock (logo, ticker, pe, volume, price, market_cap, eps, sector, employees, revenue, growth, profit) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.executemany(insert_records, contents)
        conn.commit()
    finally:
        if conn:
            conn.close()

write_csv(3)
create_connection('stonks.db')

# sqlite3 stonks.db < test.sql