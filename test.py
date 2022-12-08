import yahoo_fin.stock_info as si
import warnings
warnings. simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import sqlite3
import yfinance as yf
import csv
import numpy as np


dow_list = si.tickers_dow()
dow_stats = np.asarray([])
for ticker in dow_list:
    temp = si.get_quote_table(ticker)
    dow_stats = np.append(dow_stats, temp)

print(dow_stats.shape)
# def write_csv():
    

#     with open('test.csv', 'w+', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(headers)
#         writer.writerows(rows)

#     f.close()

# write_csv()

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

#create_connection('test.db')
#conn = sqlite3.connect('instance/stonks.sqlite')
#pd.DataFrame.to_sql('test.sql', conn, msft)