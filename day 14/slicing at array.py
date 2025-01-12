import numpy as np
arr = np.array([10, 20, 30, 40, 50])

# Access elements
print("First Element:", arr[0])  # 10
print("Last Element:", arr[-1])  # 50

# Slicing
print("First 3 Elements:", arr[:3])  # [10, 20, 30]

# Modify elements
arr[2] = 99
print("Modified Array:", arr)  # [10, 20, 99, 40, 50]
