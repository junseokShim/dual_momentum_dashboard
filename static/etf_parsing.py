import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np
import json

def yf_to_df(df, x):
    # S&P 500 2년간 데이터
    stock_data = pd.DataFrame(df.history(start=f"{x.year-2}-{x.month}-{x.day}", end=f"{x.year}-{x.month}-{x.day}"))

    new_stock_df = pd.DataFrame(stock_data.iloc[0:,:].values, columns = stock_data.columns)
    days = np.array(stock_data.index, dtype=np.datetime64)
    new_stock_df.index = [days[i].astype('str')[:10] for i in range(len(days))]
    
    return new_stock_df.to_json()


def stock_df():
    x = dt.datetime.now()
    
    # define으로 관리하고 싶은데...
    qqq = yf.Ticker("QQQ")
    spy = yf.Ticker("SPY")

    df_qqq = yf_to_df(qqq, x)
    df_spy = yf_to_df(spy, x)

    return df_qqq, df_spy


def comb(stock1, stock2, per1=0.5, per2=0.5):
    per_lst = [per1, per2]

    stock1 = pd.DataFrame(json.loads(stock1))
    stock2 = pd.DataFrame(json.loads(stock2))

    df_total = (stock1*per1 + stock2*per2)/2
    df_total = df_total.to_json()
    
    return df_total