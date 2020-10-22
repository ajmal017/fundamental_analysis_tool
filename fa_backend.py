import yfinance as yf

def get_ticker(ticker_name):
    return yf.Ticker(ticker_name)
