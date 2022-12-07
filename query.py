import sqlite3

headers = ["logo", "ticker", "pe", "volume", "price", "market_cap", "eps", "sector", "employees", "revenue", "growth", "profit"]

def find_above_size(data, index):
    if (index == 0):
        return 0
    for i in range(1,6):
         if (index - i <= 0): 
            return i
    return 5

    # index = 20
    # i want [12,13,14,15,16,17,18,19]

def find_below_size(data, index):
    if (index == len(data) - 1):
        return (0)
    for i in range(1,6):
         if (index + i >= len(data) - 1):
            return i
    return 5
    # return 2

    #index = 20
    # i want = [21,22]

def find_below_neighbors(data, index, size):
    below_neighbors = []
    for i in range(size):
        below_neighbors.append(data[index + i + 1])
    return below_neighbors

def find_above_neighbors(data, index, size):
    above_neighbors = []
    for i in range(size):
        above_neighbors.append(data[index - i - 1])
    return above_neighbors
        
            
def get_node_data(db_file, id, sort):
    conn = None
    try:
        sortIndex = headers.index(sort)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        get_data = "SELECT * FROM stock ORDER BY "
        get_data = get_data + sort
        cursor.execute(get_data)
        data = cursor.fetchall()

        index = None
        for i,row in enumerate(data):
            if (data[i][1] == id):
                index = i
            #print(i,": ",row[sortIndex], sep="")

        print(id, "at index:", index)
        print("len of data:", len(data))

        above_size = find_above_size(data, index)
        below_size = find_below_size(data, index)
        # print("above size:", above_size)
        # print("below size:", below_size)

        if (above_size < 5):
            above = find_above_neighbors(data, index, above_size)
            below_size = 10 - above_size
            below = find_below_neighbors(data, index, below_size)
        elif (below_size < 5):
            below = find_below_neighbors(data, index, below_size)
            above_size = 10 - below_size
            above = find_above_neighbors(data, index, above_size)
        else:
            below = find_below_neighbors(data, index, below_size)
            above = find_above_neighbors(data, index, above_size)

        
        print("above:", len(above))
        for i,a in enumerate(above):
            print(above[len(above)- i - 1][sortIndex])

        print("SOURCE:",data[index][sortIndex])

        print("below:", len(below))
        for i,a in enumerate(below):
            print(below[i][sortIndex])

        

    finally:
        if conn:
            conn.close()

    return data[index], above, below

