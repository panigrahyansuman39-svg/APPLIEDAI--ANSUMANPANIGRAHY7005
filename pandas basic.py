import pandas as pd
df=pd.read_csv("imdb_top_1000.csv")
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.columns)
print(df.rename(columns={'Name': 'Title'}, inplace=True)) 
print(df.columns)
