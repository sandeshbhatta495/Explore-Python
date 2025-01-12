import numpy as np
# Without vectorization (slow)
data = np.arange(1e6)
squared = [x**2 for x in data]

# With vectorization (fast)
squared_vec = data**2
