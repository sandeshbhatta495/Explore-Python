import pandas as pd

data1 = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Age': [25, 30, 35]}
data2 = {'Name': ['Alice', 'Bob', 'Charlie'],
         'Salary': [50000, 60000, 70000]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge DataFrames on the Name column
merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)
