
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Sum across rows or columns
print("Sum (all elements):", np.sum(arr))
print("Sum (columns):", np.sum(arr, axis=0))
print("Sum (rows):", np.sum(arr, axis=1))

# Cumulative sum
cumsum = np.cumsum(arr)
print("Cumulative sum:", cumsum)
