import pandas as pd
import pandas.io.data as web
import datetime

import matplotlib.pyplot as plt 
from matplotlib import style
from statistics import mean

style.use('fivethirtyeight')

start = datetime.datetime(2007,1,1)
end = datetime.datetime(2016,12,1)

att = web.DataReader("T", 'yahoo', start, end)

describe = att.describe()

att['50_close_movingAvg'] = pd.rolling_mean(att['Close'], 50)
att['10_close_movingAvg'] = pd.rolling_mean(att['Close'], 10)

att['50_close_std'] = pd.rolling_std(att['Close'], 50)
att['movingAvg_withApply'] = pd.rolling_apply(att['Close'], 50, mean)

print(att.tail())
print(50*"#")
print(att.head())
print(50*"#")

att = att.dropna(inplace=True)
print(att.head())