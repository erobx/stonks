from pyvis.network import Network
import sys
sys.path.append('../p3')
import os.path
import sqlite3
import urllib3
import numpy as np
import itertools
from queue import Queue, LifoQueue
import time

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


def init_network(db_file, net, id, sort, depth, k):
    template_path = os.path.abspath('stonks_app/templates')
    write_path = os.path.join(template_path, 'mygraph.html')

    try:
        src = init_edges(db_file, net, id, sort, depth, k)
        net.write_html(write_path)
    except (OSError, FileNotFoundError):
        print('Wrote HTML')
        return src
        

def init_edges(db_file, net, id, sort, depth, k):
    conn = None
    try:
        if depth == 0:
            return
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        query = "SELECT * FROM stock WHERE ticker = '" + id + "'"
        cursor.execute(query)
        data = cursor.fetchall()
        data = list(itertools.chain(*data))
        src = Node(data)
        
        net.add_node(src.ticker, label=src.ticker, shape="image", image=src.logo, size=10)
        inds = get_inds(db_file, id, sort, k + 1)


        for i in inds:
            query = "SELECT * FROM stock WHERE " + sort + " = " + str(i)
            cursor.execute(query)
            data = cursor.fetchall()
            data = list(itertools.chain(*data))
            newNode = Node(data)
            if newNode.ticker == src.ticker:
                continue
            net.add_node(newNode.ticker, label=newNode.ticker, shape="image", image=newNode.logo, size=10)
            net.add_edge(src.ticker, newNode.ticker)
        
        init_edges(db_file, net, data[1], sort, depth-1, k + 1)
    
        return src
    except IndexError:
        print('Empty')
    finally:
        if conn:
            conn.close()


def get_inds(db_file, id, sort, k):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        get_data = "SELECT " + sort + " FROM stock "
        cursor.execute(get_data)
        data = cursor.fetchall()
        data = list(itertools.chain(*data))
        data = np.asarray(data, dtype=float).reshape(len(data))
        
        query = "SELECT + " + sort + " FROM stock WHERE ticker = '" + id + "'"
        cursor.execute(query)
        id_v = np.asarray(cursor.fetchall())
        inds = np.argsort(abs(data-id_v))

        return data[inds[0]][1:k]
    finally:
        if conn:
            conn.close()


def bfs(src, net):
    # BASED ON STEPIK SOLUTIONS MODULE 7
    t = time.time()
    q = Queue(maxsize=0)
    visitied = []
    bfs = []

    visitied.append(src)
    q.put(src)

    while(q.empty() != True):
        current = q.get()
        bfs.append(current)

        for n in net.neighbors(current):
            if (n not in visitied):
                visitied.append(n)
                q.put(n)

    return bfs, time.time() - t


def dfs(src, net):
    # BASED ON STEPIK SOLUTIONS MODULE 7
    t = time.time()
    s = LifoQueue(maxsize=0)
    visitied = []
    dfs = []

    visitied.append(src)
    s.put(src)

    while(s.empty() != True):
        current = s.get()
        dfs.append(current)

        for n in net.neighbors(current):
            if (n not in visitied):
                visitied.append(n)
                s.put(n)

    return dfs, time.time() - t
    
