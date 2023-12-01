import yfinance as yf
import os

def download_tickers(tickers: str):
    # clear data/tickers and data/analysis
    for ticker_filename in os.listdir("data/tickers"):
        f = os.path.join("data/tickers", ticker_filename)
        if os.path.isfile(f):
            os.remove(f)
    for analysis_filename in os.listdir("data/analysis"):
        f = os.path.join("data/analysis", analysis_filename)
        if os.path.isfile(f):
            os.remove(f)

    for ticker in tickers.split("\n"):
        yf.Ticker(ticker).history(period='2y', interval='1d').to_csv(f'data/tickers/{ticker}.csv')

    return "Downloaded!"

# download_tickers(["EVN.AX"])
