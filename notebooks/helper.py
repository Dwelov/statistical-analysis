# importing the data into the python 

import pandas as pd

data = pd.read_csv("../data/Superstore.csv", encoding="latin-1")

df = data.copy()


df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')

print(df.info())