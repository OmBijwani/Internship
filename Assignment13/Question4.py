import numpy as np

arr = np.array([10, -5, 8, -12, 15])

arr[arr < 0] = 0

print(arr)