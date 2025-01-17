import numpy as np
arr = np.array([3, 1, 2, 5, 4])

# Sort the array
sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)

# Sort along rows or columns (for 2D arrays)
matrix = np.array([[3, 2, 1], [6, 5, 4]])
sorted_matrix = np.sort(matrix, axis=1)
print("Row-wise sorted:\n", sorted_matrix)
