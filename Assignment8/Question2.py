import pandas as pd 

df1 = pd.DataFrame({"Name":["Nikhil", "Om", "Parth"],
                    "ID":[35, 36, 37]}
                    , index=[0, 1, 2])

df2 = pd.DataFrame({"Name":["Piya", "Prakhar", "Prateek"],
                    "ID":[38, 39, 40]}
                    , index=[0, 1, 2])
                    
print(df1.merge(df2,on = ["ID"],how = "inner"))
print(df1.merge(df2,on = ["ID"],how = "left"))
print(df1.merge(df2,on = ["ID"],how = "right"))

result = df1.join(df2, lsuffix='_left', rsuffix='_right')
print(result)