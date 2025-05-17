import pandas as pd
data={
    "name":["hari","ram","shyam","geeta","Sheeta"],
    "age":[10,20,30,40,50],
    "city":["nagpur","badlapur","lokhanwala","butwal","colouny"]
}

data_set=pd.DataFrame(data)
print(data_set)
data_set.to_csv("output.csv",index=False)
data_set.to_json("output.json",index=False)