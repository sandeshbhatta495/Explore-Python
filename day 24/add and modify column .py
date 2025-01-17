import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Add a new column
df['Salary'] = [50000, 60000, 70000]

# Modify an existing column
df['Age'] = df['Age'] + 1

print(df)
