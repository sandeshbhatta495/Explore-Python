import pandas as pd

data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT'],
        'Salary': [50000, 60000, 55000, 52000, 62000],
        'Age': [25, 30, 29, 26, 32]}
df = pd.DataFrame(data)

# Group by Department and calculate mean salary
grouped = df.groupby('Department')['Salary'].mean()
print(grouped)

# Aggregate multiple functions
aggregated = df.groupby('Department').agg({'Salary': ['mean', 'sum'], 'Age': 'max'})
print(aggregated)
