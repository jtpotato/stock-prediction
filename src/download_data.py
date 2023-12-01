import yfinance as yf
from tickers import TICKER_LIST

for ticker in TICKER_LIST:
    yf.Ticker(ticker).history(period='max').to_csv(f'data/{ticker}.csv')