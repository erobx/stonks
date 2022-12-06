import sqlite3
def query(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        select_all = "SELECT ticker, price, sector FROM stock"
        rows = cursor.execute(select_all).fetchall()
        for r in rows:
            print(r)
    finally:
        if conn:
            conn.close()

query('stonks.db')