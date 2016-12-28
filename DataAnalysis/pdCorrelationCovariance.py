import pandas as pd
import urllib.request

urlList = [,
		   ,
		   ,
		   '']

def pickle_data():
	read = urllib.request.urlopen('https://www.quandl.com/api/v3/datasets/FBI/CRIME11.csv?api_key=EQukddx4qb4sQ4ZHSzHm')
	df = pd.read_csv.read(read)
	print(df.head())
	df.to_pickle('US_Crime.pickle')

	read = urllib.request.urlopen('https://www.quandl.com/api/v3/datasets/UKONS/LMS_LFN2_A.csv?api_key=EQukddx4qb4sQ4ZHSzHm')
	df = pd.read_csv.read(read)
	print(df.head())
	df.to_pickle('US_Employment.pickle')

	read = urllib.request.urlopen('https://www.quandl.com/api/v3/datasets/SWA/2C.csv?api_key=EQukddx4qb4sQ4ZHSzHm&start_date=1980-12-31')
	df = pd.read_csv.read(read)
	print(df.head())
	df.to_pickle('US_Income.pickle')

	read = urllib.request.urlopen('https://www.quandl.com/api/v3/datasets/ODA/USA_NGDPD.csv?api_key=EQukddx4qb4sQ4ZHSzHm')
	df = pd.read_csv.read(read)
	print(df.head())
	df.to_pickle('US_GDP.pickle')

pickle_data()

df1 = pd.read_pickle('US_Crime.pickle')
df2 = pd.read_pickle('US_Employment.pickle')
df3 = pd.read_pickle('US_Income.pickle')
df4 = pd.read_pickle('US_GDP.pickle')

df2.columns = ['Year', 'Employment_Rate']
df4 = df4.rename(columns={'Date':'Year', 'Value':'GDP_Cap'})

df.set_index('Year',inplace=True)
df2.set_index('Year',inplace=True)
df3.set_index('Year',inplace=True)
df4.set_index('Year',inplace=True)

joined = df.join([df2,df3,df4])

print(joined.head())
print(75*'#')

print(joined.corr())
print(75*'#')

print(joined.cov())