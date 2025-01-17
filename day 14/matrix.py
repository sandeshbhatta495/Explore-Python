import numpy as np
import random
arr1 = np.array([random.randint(1, 9)])
arr2 = np.array([random.randint(1, 9)])
arr3 = np.array([random.randint(1, 9)])
print("matrix 1:", arr1)
print("matrix 2:", arr2)
print("matrix 3:", arr3)
arr4 = np.random.randint(1, 10, size=(3, 3))
print("Random 3x3 Matrix:", arr4)

# Compute sum, mean, and max of arr4
sum_arr4 = np.sum(arr4)
mean_arr4 = np.mean(arr4)
max_arr4 = np.max(arr4)

print("Sum of arr4:", sum_arr4)
print("Mean of arr4:", mean_arr4)
print("Max of arr4:", max_arr4)