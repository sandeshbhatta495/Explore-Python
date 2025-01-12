import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Save to .npy file
np.save('array.npy', arr)

# Load from file
loaded_arr = np.load('array.npy')
print("Loaded array:\n", loaded_arr)
