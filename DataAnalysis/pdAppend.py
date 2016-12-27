import pandas as pd 

df1 = pd.DataFrame({'Temp':[75,73,72,68],
					'Humidity':[55,60,72,58],
					'Precip':[0,0,0,25]},
					index=[0,1,2,3])

df2 = pd.DataFrame({'Temp':[42,57,55,48],
					'Humidity':[35,40,42,37],
					'Precip':[2,0,5,2]},
					index=[0,1,2,3])

df3 = pd.DataFrame({'Temp':[65,68,72,63],
					'Humidity':[40,45,38,35],
					'Precip':[0,15,0,5]},
					index=[0,1,2,3])

df4 = pd.DataFrame({'Temp':[42,57,55,48],
					'Humidity':[35,40,42,37],
					'Wind':[15,12,7,22]},
					index=[0,1,2,3])

df5 = pd.DataFrame({'Pressure':[12,15,15,13],
					'Cloudy':[15,25,40,37],
					'Wind':[15,12,7,22]},
					index=[0,1,2,3])

appended = df1.append(df2)
print(appended)
print(50*"#")

values = [81, 35, 0]

s = pd.Series(values, index=['Temp','Humidity','Precip'])

df3 = df3.append(s, ignore_index=True)
print(df3)