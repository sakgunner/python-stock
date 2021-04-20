import yfinance as yf

from time import time, sleep


def main():
    ticker = yf.Ticker("TDEX.BK")
    his = ticker.history(period="1d", interval="1m", auto_adjust=False, actions=False)
    print(len(his))
    print(his.tail(1))

main()
