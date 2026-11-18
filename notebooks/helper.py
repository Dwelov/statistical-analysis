# importing the data into the python 

import pandas as pd
import os

data = pd.read_csv("../data/Superstore.csv", encoding="latin-1")
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, "..", "data", "Superstore.csv")

data = pd.read_csv(data_path, encoding="latin-1")

df = data.copy()

# Select columns J, K, M, O, P, R, S, T, U (0-indexed: 9, 10, 12, 14, 15, 17, 18, 19, 20)
# J: City, K: State, M: Region, O: Category, P: Sub-Category, R: Sales, S: Quantity, T: Discount, U: Profit


selected_columns = ['City', 'State', 'Region', 'Category', 'Sub-Category', 'Sales', 'Quantity', 'Discount', 'Profit']
selected_df = df[selected_columns]

print(selected_df)