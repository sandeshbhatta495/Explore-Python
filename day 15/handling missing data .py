import numpy as np
arr = np.array([1, 2, np.nan, 4])

# Check for NaN values
print("Is NaN:", np.isnan(arr))

# Replace NaN with a value
arr[np.isnan(arr)] = 0
print("Replaced NaN:", arr)

# Calculate ignoring NaN
mean = np.nanmean(arr)
print("Mean ignoring NaN:", mean)
