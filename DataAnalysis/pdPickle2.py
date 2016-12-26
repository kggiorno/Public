import pandas as pd
import urllib.request
import pickle

depth_json = urllib.request.urlopen('https://btc-e.com/api/3/depth/btc_usd').read()
depth_df = pd.read_json(depth_json)
depth_df.to_pickle('pickle_example.pickle')
newdf = pd.read_pickle('pickle_example.pickle')

#print(newdf.head())

pickle_out = open('newdf.pickle','wb')
pickle.dump(newdf, pickle_out)
pickle_out.close()

pickle_in = open('newdf.pickle','rb')
imported_pickle = pickle.load(pickle_in)

print(imported_pickle)
print(imported_pickle.head())


