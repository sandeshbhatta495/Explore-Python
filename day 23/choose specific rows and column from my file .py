import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Select a specific column
print(df['Name'])

# Select a specific row
print(df.loc[1])

# Select specific rows and columns
print(df.loc[0:1, ['Name', 'City']])
