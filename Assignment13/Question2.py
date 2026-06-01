import numpy as np

arr = np.arange(24).reshape(2, 3, 4)

print("Original Shape:", arr.shape)

new_arr = np.moveaxis(arr, 0, 2)

print("New Shape:", new_arr.shape)
print(new_arr)