import numpy as np
from PIL import Image

# Load an image as a NumPy array
img = Image.open("example.jpg")
img_array = np.array(img)

# Modify the image (invert colors)
inverted = 255 - img_array

# Convert back to image and save
inverted_img = Image.fromarray(inverted)
inverted_img.save("inverted_example.jpg")
