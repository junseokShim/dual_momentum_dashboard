import yfinance as yf
import datetime as dt

def update(x):
    
    qqq = yf.Ticker("QQQ")
    spy = yf.Ticker("SPY")

    # QQQ 1년간 데이터
    qqq_data = qqq.history(start=f"{x.year-1}-{x.month}-{x.day}",
                            end=f"{x.year}-{x.month}-{x.day}")

    # SPY 1년간 데이터
    spy_data = spy.history(start=f"{x.year-1}-{x.month}-{x.day}", 
                            end=f"{x.year}-{x.month}-{x.day}")
    
    return qqq_data, spy_data