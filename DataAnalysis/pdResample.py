import pandas as pd 
import urllib.request
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('fivethirtyeight')

df = pd.read_pickle('AAPL.pickle')
df.sort('Date', inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print(df.head())
print(75*'#')

df2 = df.resample('3D').mean()
print(df2.head())
print(75*'#')

df3 = df.resample('1M').mean()
print(df3.head())
print(75*'#')

df4 = df.resample('12M').mean()
print(df3.head())

df4['Adjusted Close'].plot()
df3['Adjusted Close'].plot()
df2['Adjusted Close'].plot()
df['Adjusted Close'].plot()
plt.show()

'''
Alias	Description
B	business day frequency
C	custom business day frequency (experimental)
D	calendar day frequency
W	weekly frequency
M	month end frequency
SM	semi-month end frequency (15th and end of month)
BM	business month end frequency
CBM	custom business month end frequency
MS	month start frequency
SMS	semi-month start frequency (1st and 15th)
BMS	business month start frequency
CBMS	custom business month start frequency
Q	quarter end frequency
BQ	business quarter endfrequency
QS	quarter start frequency
BQS	business quarter start frequency
A	year end frequency
BA	business year end frequency
AS	year start frequency
BAS	business year start frequency
BH	business hour frequency
H	hourly frequency
T, min	minutely frequency
S	secondly frequency
L, ms	milliseconds
U, us	microseconds
N	nanoseconds
'''