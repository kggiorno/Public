import pandas as pd
import pandas.io.data as web
import datetime

import matplotlib.pyplot as plt 
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2007,1,1)
end = datetime.datetime(2016,12,1)

att = web.DataReader("T", 'yahoo', start, end)

print(att.head())
print(50*"#")

att['Open_div_10'] = att['Open'] / 10
att['High_minus_low'] = att['High'] - att['Low']

print(att.head())

