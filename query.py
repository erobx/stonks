import sqlite3

# logo, ticker, pe, volume, price, market_cap, eps, sector, employees, revenue, growth, profit

def query_first5_at_ticker(db_file, id):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        find_ticker = "SELECT rowid, ticker, volume FROM stock ORDER BY volume DESC"
        cursor.execute(find_ticker)  
        data = cursor.fetchall()

        index = None
        for i,r in enumerate(data):
            if (data[i][1] == id):
                index = i
            print(r)

        print("ticker at index:", index)

    finally:
        if conn:
            conn.close()
query_first5_at_ticker('stonks.db', 'CVE')