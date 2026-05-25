import pandas as pd

data = {
    "Name": ["Om", "Rahul", "Aman", "Neha"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()


# 1. Different Ways to Iterate Over Rows

print("Using iterrows():")
for index, row in df.iterrows():
    print(index, row["Name"], row["Marks"])
print()

print("Using itertuples():")
for row in df.itertuples():
    print(row.Name, row.Age, row.Marks)
print()

# 2. Selecting Rows Based on Conditions

print("Students with Marks > 80:")
result = df[df["Marks"] > 80]
print(result)
print()

# 3. Select Any Row Using iloc[]

print("First Row using iloc:")
print(df.iloc[0])
print()

print("Second and Third Rows:")
print(df.iloc[1:3])
print()

# 4. Limited Rows Selection with Given Column

print("Only Name column for first 2 rows:")
print(df.loc[0:1, ["Name"]])
print()

print("Name and Marks columns:")
print(df.loc[:, ["Name", "Marks"]])
print()

# 5. Drop Rows Based on Condition

print("Drop rows where Marks < 80:")

df_filtered = df[df["Marks"] >= 80]

print(df_filtered)
print()

# 6. Insert Row at Given Position

new_row = {
    "Name": "Karan",
    "Age": 24,
    "Marks": 88
}

top = df.iloc[:2]
bottom = df.iloc[2:]

new_df = pd.concat([top, pd.DataFrame([new_row]), bottom]).reset_index(drop=True)

print("DataFrame after inserting new row:")
print(new_df)
print()

# 7. Create List from Rows in DataFrame

print("Convert rows to list:")

row_list = df.values.tolist()

print(row_list)
print()