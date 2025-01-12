import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]}
df = pd.DataFrame(data)

# Save DataFrame to a CSV file
df.to_csv('example.csv', index=False)
print("Data saved to example.csv")

# Load the saved CSV file
loaded_df = pd.read_csv('example.csv')
print(loaded_df)
