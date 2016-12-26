import pandas as pd
import datetime
import pandas.io.data as web

import matplotlib.pyplot as pyplot
from matplotlib import style

style.use('fivethirtyeight')

starting = {'Col_1':[5,2,4,7],
			'Col_2':[7,8,2,1],
			'Col_3':[10,4,2,6],
			'Col_4':[5,7,3,5],
			'Col_5':[9,9,2,1],
			'Col_6':[7,3,5,10],
			}

df = pd.DataFrame(starting)
print(df)
print(df.dtypes)

