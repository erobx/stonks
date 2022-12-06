import sqlite3

# logo, ticker, pe, volume, price, market_cap, eps, sector, employees, revenue, growth, profit

def query(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        select_all = "SELECT logo, ticker, volume, price, sector FROM stock"
        rows = cursor.execute(select_all).fetchall()
        for r in rows:
            print(r)
    finally:
        if conn:
            conn.close()

query('stonks.db')