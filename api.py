'''
This is to test the yfinance module and see how it structures the data
'''
import pandas as pd
from yahoo_fin import stock_info as si
import csv
import numpy as np
import yfinance as yf

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

headers = ['ticker', 'trailingPE', 'averageVolume', 'regularMarketPrice', 
            'marketCap', 'forwardPE', 'sector', 'fullTimeEmployees', 
            'logo_url', 'grossProfits', 'dividendRate', 'earningsGrowth']

# rows = np.asarray([])
# for ticker in tickers:
#     t = yf.Ticker(ticker).info
#     info = np.asarray([t[i] for i in headers[1:] if t[i] in t])
#     rows = np.append(rows, info)

# tickers_data = {}
# for i in tickers[:5]:
#     ticker_object = yf.Ticker(i)

#     #convert info() output from dictionary to dataframe
#     temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
#     temp.reset_index(inplace=True)
#     temp.columns = ["Attribute", "Recent"]
    
#     # add (ticker, dataframe) to main dictionary
#     tickers_data[i] = temp

# combined_data = pd.concat(tickers_data)
# combined_data = combined_data.reset_index()
# employees = combined_data[combined_data["Attribute"]=="trailingPE"].reset_index()
# del employees["level_1"]
# del employees["index"]  # clean up unnecessary column
# employees.columns =("Ticker", "Attribute", "Recent")
# print(employees)

#rows = np.reshape(rows, (len(rows), len(headers)))

# with open('tickers.csv', 'w+', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(headers)
#     writer.writerows(rows)

# f.close()