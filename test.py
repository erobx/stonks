import yfinance as yf

msft = yf.Ticker("MSFT").info
for i in msft:
    print(i)