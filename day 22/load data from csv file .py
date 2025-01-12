import pandas as pd

# Sample CSV loading (replace 'your_file.csv' with an actual file)
# df = pd.read_csv('your_file.csv')
# Simulating a CSV load with dictionary data
data = {'Product': ['Laptop', 'Phone', 'Tablet'],
        'Price': [1000, 500, 300],
        'Quantity': [10, 20, 15]}
df = pd.DataFrame(data)
print(df)
