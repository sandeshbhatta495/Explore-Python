import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Add a scalar to every element
print(arr + 10)

# Add a 1D array to each row
row_add = np.array([1, 2, 3])
print(arr + row_add)

# Add a column vector to each column
col_add = np.array([[1], [2]])
print(arr + col_add)
