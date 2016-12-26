import pandas as pd

df = pd.read_csv('FBI-CRIME11.csv')
df.set_index('Year', inplace=True)
df['Violent Crime Rate'].to_csv('VCRate.csv')


df = pd.read_csv('VCRate.csv')


print(df.head())