

import pandas as pd


url_df = pd.read_csv('/Users/bradhicks/Desktop/2020urldf.csv')
print(list(url_df.columns.values))

print(url_df)

#print(url_df['Subsidiary List URL'])

url_df = url_df.drop_duplicates(subset=['Company Name'])
print(url_df)