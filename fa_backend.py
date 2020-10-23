import yfinance as yf

class FinanceException(Exception):
    pass

class TickerNotFoundException(FinanceException):
    pass

currencies = {"EUR": "€",
              "USD": "$"}

def get_ticker(ticker_name):
    if not (ticker_name and len(ticker_name) >= 4):
        raise TickerNotFoundException

    try:
        return yf.Ticker(ticker_name)
    except Exception as ex:
        raise TickerNotFoundException from ex

def get_name(ticker):
    return ticker.info["shortName"]

def get_symbol(ticker):
    return ticker.info["symbol"]

def get_currency(ticker):
    return ticker.info["currency"]

def get_ask(ticker):
    return ticker.info["ask"]

def get_bid(ticker):
    return ticker.info["bid"]

def get_eps_trailing(ticker):
    return ticker.info["trailingEps"]

def get_eps_forward(ticker):
    return ticker.info["forwardEps"]

def get_askbid_spread(ticker):
    return get_ask(ticker) - get_bid(ticker)

def get_formatted_floatstring(number):
    return "{:.2f}".format(number)

def get_formatted_currencystring(number, currency):
    try:
        result = "{:.2f}{}".format(number, currencies[currency])
    except TypeError:
        result = "N/A"

    return result

# testticker = get_ticker("MSFT")
# for name, value in testticker.info.items():
#     print("{:<50} {}".format(name, value))
