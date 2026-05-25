import pandas as pd

# 1. DataFrame from Two-Dimensional Python List

data1 = [
    [1, "Om", 21],
    [2, "Rahul", 22],
    [3, "Aman", 20]
]

df1 = pd.DataFrame(data1)

print("DataFrame from Two-Dimensional List:")
print(df1)
print()

# 2. DataFrame from Python Dictionary

data2 = {
    "Name": ["Om", "Rahul", "Aman"],
    "Age": [21, 22, 20],
    "City": ["Jaipur", "Delhi", "Mumbai"]
}

df2 = pd.DataFrame(data2)

print("DataFrame from Dictionary:")
print(df2)
print()

# 3. DataFrame from List of Lists

data3 = [
    ["Om", 21],
    ["Rahul", 22],
    ["Aman", 20]
]

df3 = pd.DataFrame(data3, columns=["Name", "Age"])

print("DataFrame from List of Lists:")
print(df3)
print()

# 4. DataFrame from List of Tuples

data4 = [
    ("Om", 21),
    ("Rahul", 22),
    ("Aman", 20)
]

df4 = pd.DataFrame(data4, columns=["Name", "Age"])

print("DataFrame from List of Tuples:")
print(df4)
print()

# 5. DataFrame from List of Dictionaries

data5 = [
    {"Name": "Om", "Age": 21},
    {"Name": "Rahul", "Age": 22},
    {"Name": "Aman", "Age": 20}
]

df5 = pd.DataFrame(data5)

print("DataFrame from List of Dictionaries:")
print(df5)
print()