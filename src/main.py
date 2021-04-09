import yfinance as yf

from time import time, sleep


if __name__ == "__main__":
    print("hello world!!!")
    # while True:
    aapl = yf.Ticker("TDEX.BK")
    his = aapl.history(period="1d", interval="1m", prepost=True, auto_adjust=False, actions=False)
    print(his)
        # print(f'{aapl.info["longName"]}: {aapl.info["ask"]} --- {aapl.info["bid"]} --- {aapl.info["regularMarketPrice"]}')
        # sleep(60 - time() % 60)
