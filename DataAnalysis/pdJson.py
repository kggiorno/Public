import pandas as pd

df = pd.read_hdf('hdfstore.h5','d1')

df.to_json('example_json.json')

df2 = pd.read_json('example_json.json')

print(df2.head())

