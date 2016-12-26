import pandas as pd
import pandas.io.data as web
import datetime

import matplotlib.pyplot as plt 
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2007,1,1)
end = datetime.datetime(2016,12,1)

att = web.DataReader("T", 'yahoo', start, end)

describe = att.describe()

att['50_close_movingAvg'] = pd.rolling_mean(att['Close'], 50)
att['10_close_movingAvg'] = pd.rolling_mean(att['Close'], 10)

fig, axes = plt.subplots(nrows=2, ncols=1)

att['50_close_std'] = pd.rolling_std(att['Close'], 50)
att['50_close_std'].plot(ax=axes[1], label='50_close_std')

att['Close'].plot(ax=axes[0], label='Price')
att['50_close_movingAvg'].plot(ax=axes[0], label='50_close_movingAvg')
att['10_close_movingAvg'].plot(ax=axes[0], label='10_close_movingAvg')
plt.legend(loc=4)

plt.show()

