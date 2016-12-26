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
print(describe)
print(50*"#")
print(describe['Open'])
openStdDev = describe['Open']['std']
print(openStdDev)



