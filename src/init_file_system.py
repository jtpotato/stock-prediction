import os

def initialise_filesystem():
    if not os.path.exists("data/tickers"):
        print("[jtpotato/stock-prediction] Creating data/tickers folder")
        os.makedirs("data/tickers")
    if not os.path.exists("data/analysis"):
        print("[jtpotato/stock-prediction] Creating data/analysis folder")
        os.makedirs("data/analysis")