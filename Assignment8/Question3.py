import pandas as pd 

df1 = pd.DataFrame({"Name":["Nikhil", "Om", "Parth"],
                    "ID":[35, 36, 37]})

df2 = pd.DataFrame({"Name":["Piya", "Prakhar", "Prateek"],
                    "ID":[38, 39, 40,]})

df3 = pd.DataFrame({"Name":["Om", "Nikhil", "Shresth"],
                    "ID":[36, 35, 51]})

result = pd.concat([df1, df2], ignore_index=False)
print(result)

print(result.merge(df3,on=["ID"]))