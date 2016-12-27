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

concat = pd.concat([df1,df2,df3])
print(concat)
print(50*'#')

concat2 = pd.concat([df1,df2,df4])
print(concat2)
print(50*'#')

concat3 = pd.concat([df1,df2,df5], axis=1)
print(concat3)