import numpy as np

# Two 2D arrays
arr1 = np.array([[3, 4],
                 [5, 6]])

arr2 = np.array([[1, 0],
                 [7, 8]])

# Average of arrays
avg = (arr1 + arr2) / 2

print("Average Array:")
print(avg)

# Combine all elements into a single array
combined = np.concatenate((arr1.flatten(), arr2.flatten()))

# Mean
mean = np.mean(combined)

# Median
median = np.median(combined)

# Mode using NumPy only
values, counts = np.unique(combined, return_counts=True)
mode = values[np.argmax(counts)]

print("\nMean =", mean)
print("Median =", median)
print("Mode =", mode)