import pandas as pd

data = pd.read_csv("lifepatch_synthetic_donors_nepal_with_coords.csv",encoding="latin1")
print(data.head())
print(data.info())
print("hello wrold ")