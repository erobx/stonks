'''
This is to test the yfinance module and see how it structures the data
'''
import yfinance as yf

msft = yf.Ticker("MSFT").info

print(msft['volume'])
print(msft['forwardPE'])