import yahoo_fin.stock_info as si
import warnings
warnings. simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import sqlite3
import yfinance as yf
import csv
import numpy as np

def write_csv():
    # 1
    yf_header = ['logo_url', 'ticker']
    # 5
    si_quote_headers = [
                'PE Ratio (TTM)', 'Avg. Volume', 'Previous Close',
                'Market Cap', 'EPS (TTM)']
    # 2
    si_info_headers = ['sector', 'fullTimeEmployees']
    # 3
    si_stats_headers = ['Revenue (ttm)', 'Quarterly Revenue Growth', 'Gross Profit (ttm)']

    headers = yf_header + si_quote_headers + si_info_headers + si_stats_headers

    tickers = ['PEI$B', 'AVB.S', 'MSFT', 'FTNT', 'V', 'S']

    rows = []
    for t in tickers:
        if (t.find('$') != -1):
            continue
        elif (t.find('.') != -1):
            continue
        print(t)
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
                values.append('0')

        for h in si_stats_headers:
            value = stats[stats['Attribute']==h].reset_index()
            if not value.empty:
                value = value.iloc[0]['Value']
                values.append(value)
            else:
                values.append('0')

        rows.append(values)

    rows = np.asarray(rows)
    rows = np.reshape(rows, (len(rows), len(headers)))

    with open('test.csv', 'w+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    f.close()

write_csv()

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        file = open('test.csv')
        contents = csv.reader(file)
        insert_records = "INSERT INTO stock (logo, ticker, pe, volume, price, market_cap, eps, sector, employees, revenue, growth, profit) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.executemany(insert_records, contents)
        select_all = "SELECT ticker, price, sector FROM stock"
        rows = cursor.execute(select_all).fetchall()

        for r in rows:
            print(r)
        conn.commit()
    finally:
        if conn:
            conn.close()

create_connection('test.db')
#conn = sqlite3.connect('instance/stonks.sqlite')
#pd.DataFrame.to_sql('test.sql', conn, msft)