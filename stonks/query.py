import sqlite3
import numpy as np
from scipy import spatial

headers = ["logo", "ticker", "pe", "volume", "price", "market_cap", "eps", "sector", "employees", "revenue", "growth", "profit"]

# def find_above_size(data, index):
#     if (index == 0):
#         return 0
#     for i in range(1,6):
#          if (index - i <= 0): 
#             return i
#     return 5

# def find_below_size(data, index):
#     if (index == len(data) - 1):
#         return (0)
#     for i in range(1,6):
#          if (index + i >= len(data) - 1):
#             return i
#     return 5

# def find_below_neighbors(data, index, size):
#     below_neighbors = []
#     for i in range(size):
#         below_neighbors.append(data[index + i + 1])
#     return below_neighbors

# def find_above_neighbors(data, index, size):
#     above_neighbors = []
#     for i in range(size):
#         above_neighbors.append(data[index - i - 1])
#     return above_neighbors
        
            



        # index = None
        # for i,row in enumerate(data):
        #     if (data[i][1] == id):
        #         index = i
            #print(i,": ",row[sortIndex], sep="")

    #     above_size = find_above_size(data, index)
    #     below_size = find_below_size(data, index)
    #     # print("above size:", above_size)
    #     # print("below size:", below_size)

    #     if (above_size < 5):
    #         above = find_above_neighbors(data, index, above_size)
    #         below_size = 10 - above_size
    #         below = find_below_neighbors(data, index, below_size)
    #     elif (below_size < 5):
    #         below = find_below_neighbors(data, index, below_size)
    #         above_size = 10 - below_size
    #         above = find_above_neighbors(data, index, above_size)
    #     else:
    #         below = find_below_neighbors(data, index, below_size)
    #         above = find_above_neighbors(data, index, above_size)

        
    

    # return data[index], above, below

