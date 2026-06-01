import numpy as np

arr = np.array([[10, np.nan, 30],
                [20, 40, np.nan],
                [30, 50, 60]])

# Column means
col_mean = np.nanmean(arr, axis=0)

# Find NaN positions
inds = np.where(np.isnan(arr))

# Replace NaN with column mean
arr[inds] = np.take(col_mean, inds[1])

print(arr)