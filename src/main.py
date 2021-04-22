import yfinance as yf

from sklearn.svm import SVR
from time import sleep


def SMA(data, period=30, column="Close"):
    return data[column].rolling(window=period).mean()


def EMA(data, period=20, column="Close"):
    return data[column].ewm(span=period, adjust=False).mean()


def MACD(data, period_short=12, period_long=26, period_signal=9, column="Close"):
    short_ema = EMA(data, period_short, column=column)
    long_ema = EMA(data, period_long, column=column)
    data["MACD"] = short_ema - long_ema
    data["Signal_Line"] = EMA(data, period_signal, column="MACD")
    return data


def RSI(data, period=14, column="Close"):
    delta = data[column].diff(1)
    delta = delta[1:]
    up = delta.copy()
    down = delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    data['up'] = up
    data['down'] = down
    AVG_Gain = SMA(data, period, column="up")
    AVG_Loss = abs(SMA(data, period, column="down"))
    RS = AVG_Gain / AVG_Loss
    RSI = 100.0 - (100.0/(1.0 + RS))
    data["RSI"] = RSI
    return data


def technical():
    ticker = yf.Ticker("DELTA.BK")
    """
    period : str
        Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        Either Use period parameter or use start and end
    interval : str
        Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        Intraday data cannot extend last 60 days
    """
    his = ticker.history(period="max", interval="1d", auto_adjust=False, actions=False)
    MACD(his)
    RSI(his)
    his["SMA"] = SMA(his)
    his["EMA"] = EMA(his)
    # print(his["Close"].rolling(window=30).mean())
    print(his.tail(1))
    # print(his)


def predict():
    ticker = yf.Ticker("DELTA.BK")
    """
    period : str
        Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        Either Use period parameter or use start and end
    interval : str
        Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        Intraday data cannot extend last 60 days
    """
    his = ticker.history(period="3mo", interval="1d", auto_adjust=False, actions=False)
    days = list()
    adj_close_prices = list()
    df_adj_close = his.loc[:, "Adj Close"]
    for i in range(len(his)):
        days.append([i+1])
    for adj_close_price in df_adj_close:
        adj_close_prices.append(float(adj_close_price))
    lin_svr = SVR(kernel="linear", C=1000.0)
    lin_svr.fit(days, adj_close_prices)
    poly_svr = SVR(kernel="poly", C=1000.0, degree=2)
    poly_svr.fit(days, adj_close_prices)
    rbf_svr = SVR(kernel="rbf", C=1000.0, gamma=0.85)
    rbf_svr.fit(days, adj_close_prices)
    day = [[len(his)+1]]
    print("RBF SVR predicted price", rbf_svr.predict(day))
    print("Linear SVR predicted price", lin_svr.predict(day))
    print("Polynomial SVR predicted price", poly_svr.predict(day))


if __name__ == "__main__":
    # while True:
    #     main()
    #     sleep(60)
    technical()
    predict()
