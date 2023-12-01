import pandas as pd
from prophet import Prophet
import os

def predict_all():
    img_paths = []

    for ticker_filename in os.listdir("data/tickers"):
        f = os.path.join("data/tickers", ticker_filename)
        if os.path.isfile(f):
            print("[jtpotato/stock-prediction] Running analysis on: " + f)
            df = pd.read_csv(f)

            simple_df = pd.DataFrame()
            simple_df['ds'] = pd.to_datetime(df['Date'], utc=True).dt.tz_localize(None)
            simple_df['y'] = df['Close']

            m = Prophet(scaling='minmax', growth='linear', n_changepoints=48, mcmc_samples=0)
            m.fit(simple_df)

            future = m.make_future_dataframe(periods=28)
            forecast = m.predict(future)

            fig1 = m.plot(forecast)
            ax = fig1.gca()
            ax.set_title('Stock price prediction for ' + ticker_filename)

            ax.set_xlim(simple_df['ds'].take([-100]), pd.to_datetime('now') + pd.DateOffset(days=28))

            fig1.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
            fig1.savefig('data/analysis/' + ticker_filename + '.jpg')
            img_paths.append('data/analysis/' + ticker_filename + '.jpg')

    return img_paths