from pyvis.network import Network
import sys
sys.path.append('../p3')
import os.path
import sqlite3
import urllib3
from scipy import spatial
import numpy as np


# 1. logo, 2. ticker, 3. pe, 4. volume, 5. price, 6. market_cap, 7. eps, 8. sector, 9. employees, 10. revenue, 11. growth, 12. profit


class Node():
    def __init__(self, info):
        if (info[0] == 'none'):
            self.logo = 'static/images/stonks.jpeg'
        else:
            http = urllib3.PoolManager()
            error = http.request('GET', info[0])
            if (error.status == 404):
                self.logo = 'static/images/stonks.jpeg'
            else:
                self.logo = info[0]
        self.ticker = info[1]
        self.pe = info[2]
        self.volume = info[3]
        self.price = info[4]
        self.market_cap = info[5]
        self.eps = info[6]
        self.sector = info[7]
        self.employees = info[8]
        self.revenue = info[9]
        self.growth = info[10]
        self.profit = info[11]

    def getVal(self, sort):
        if sort == 'logo':
            return self.logo
        if sort == 'ticker':
            return self.ticker
        if sort == 'pe':
            return self.pe
        if sort == 'volume':
            return self.volume
        if sort == 'price':
            return self.price
        if sort == 'market_cap':
            return self.market_cap
        if sort == 'eps':
            return self.eps
        if sort == 'sector':
            return self.sector
        if sort == 'employees':
            return self.employees
        if sort == 'revenue':
            return self.revenue
        if sort == 'growth':
            return self.growth
        if sort == 'profit':
            return self.profit


def init_network(db_file, id, sort):
    template_path = os.path.abspath('stonks/templates')
    write_path = os.path.join(template_path, 'mygraph.html')
    print(write_path)
    net = Network(height="100vh", neighborhood_highlight=True)
    net.toggle_physics(True)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        #source node
        query = "SELECT * FROM stock WHERE ticker = '" + id + "'"
        cursor.execute(query)
        data = cursor.fetchall()[0]
        src = Node(data)
        #print("SRC:", src.ticker)
        net.add_node(src.ticker, label=src.ticker, shape="image", image=src.logo)

        inds = get_inds(db_file, id, sort)

        for i in inds:
            if i == 0:
                continue
            query = "SELECT * FROM stock WHERE rowid = " + str(i)
            cursor.execute(query)
            data = [j for j in cursor.fetchall()[0]]
            newNode = Node(data)
            net.add_node(newNode.ticker, label=newNode.ticker, shape="image", image=newNode.logo)
            #diff = abs(newNode.getVal(sort) - src.getVal(sort))
            net.add_edge(src.ticker, newNode.ticker)

    finally:
        try:
            net.write_html(write_path)
            if conn:
                conn.close()
        except (OSError, FileNotFoundError):
            print('Error')
        

def get_inds(db_file, id, sort):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        get_data = "SELECT volume FROM stock "
        get_data = get_data + sort
        cursor.execute(get_data)
        data = np.asarray(cursor.fetchall())
        
        query = "SELECT + " + sort + " FROM stock WHERE ticker = '" + id + "'"
        cursor.execute(query)
        id_v = np.asarray(cursor.fetchall())
        tree = spatial.KDTree(data)
        k = 6
        _, inds = tree.query(id_v, k)
        return inds.reshape(-1)[1:]
    finally:
        if conn:
            conn.close()


# db_path = os.path.abspath('stonks/stonks.db')
# init_network(db_path, 'DTF', 'volume')