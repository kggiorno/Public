import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

bridge_readings = {'Distance_mm': [50012, 50015, 50009, 5024012, 50007, 50016, 50014]}

df = pd.DataFrame(bridge_readings)
#df.plot()
#plt.show()

stats = df.describe()
df['std'] = pd.rolling_std(df['Distance_mm'],2)
print(df.head())
print(50*"#")

df = df[(df['std'] < stats.Distance_mm['std'])]

print(df.head())
print(50*"#")

df = df[(df['std'] < 50)]
print(df.head())
print(50*"#")

df['Distance_mm'].plot()
plt.show()