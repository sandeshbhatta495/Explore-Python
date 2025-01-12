import numpy as np
np.random.seed(42)  # Set the seed for reproducibility

# Generate random integers
rand_ints = np.random.randint(1, 10, size=(2, 3))
print("Random integers:\n", rand_ints)

# Shuffle an array
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print("Shuffled array:", arr)
