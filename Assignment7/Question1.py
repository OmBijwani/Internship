import pandas as pd

#Dictionary

print("DICTIONARY: ")
d = {
    "a": 10,
    "b": 20,
    "c": 30
}

series_d = pd.Series(d)

print(series_d)
print(series_d["a"])

#List

print("LIST: ")

labels = ["a", "b", "c"]
l = [1, 2, 3]
series_l = pd.Series(l, index= labels)
print(series_l)
print(series_l["a"])



