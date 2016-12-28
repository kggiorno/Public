import pandas as pd 
import urllib.request

school = {'Name':['Jimmy','Ashley','Joe','Sarah','Terrence','Shelby','Elias','Kelsey','Michael','Amy'],
		  'Age':[18,17,19,15,17,16,16,15,15,18],
		  'Grade':[12,10,12,10,9,9,10,9,9,12]}

df = pd.DataFrame(school)
print(df)
print(50*'#')

df2 = df.sort('Age')
print(df2)
print(50*'#')

df2 = df.sort(['Grade','Age'])
print(df2)
print(50*'#')

df2 = df.sort(['Grade','Age','Name'])
print(df2)
print(50*'#')

df2 = df.sort(['Grade','Age','Name'], ascending=False)
print(df2)
print(50*'#')

df2 = df.sort(['Grade','Age','Name'], ascending=[False,False,True])
print(df2)
print(50*'#')