import pandas as pd 
import urllib.request

import matplotlib.pyplot as plt

def pickle_data():
	read = urllib.request.urlopen('https://www.quandl.com/api/v3/datasets/YAHOO/AAPL.csv?api_key=EQukddx4qb4sQ4ZHSzHm')
	df = pd.read_csv(read)
	df.to_pickle('AAPL.pickle')

df = pd.read_pickle('AAPL.pickle')
df.sort('Date', inplace=True)
df.set_index('Date', inplace=True)
df = df['Adjusted Close']
print(df.head())
print(50*'#')

df.plot()
plt.show()
