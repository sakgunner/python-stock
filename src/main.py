import yfinance as yf

from time import sleep


def main():
    ticker = yf.Ticker("TDEX.BK")
    """
    period : str
        Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        Either Use period parameter or use start and end
    interval : str
        Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        Intraday data cannot extend last 60 days
    """
    his = ticker.history(period="5d", interval="1m", auto_adjust=False, actions=False)
    print(his.tail(1))

if __name__ == "__main__":
    while True:
        main()
        sleep(60)
