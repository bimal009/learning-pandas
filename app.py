import pandas as pd

# data=pd.read_csv("sales_data_sample.csv",encoding="latin1")
data=pd.read_json("sample.json")
print(data)