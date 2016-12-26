import pandas as pd
import datetime
import pandas.io.data as web

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 12, 15)

att = web.DataReader("T", "yahoo", start, end)

print(att.head())

#highsList = att['High'].tolist()

att[['High','Low','Adj Close']].plot()
plt.legend()
plt.show()

