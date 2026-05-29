#Q1 Replace NaN with 0 and interchange rows/columns
import numpy as np

arr = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])

# Replace NaN with 0
arr = np.nan_to_num(arr, nan=0)

print("After Replacing NaN:")
print(arr)

# Interchange rows and columns
res = arr.T

print("\nTranspose Matrix:")
print(res)

#Q2 Move axes of 3D array
import numpy as np

arr = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])


print(arr)

res = np.moveaxis(arr, 0, -1)


print(res)
#Q3 Replace NaN with column average
import numpy as np

arr = np.array([
    [1,2,np.nan],
    [4,np.nan,6],
    [7,8,9]
])

# Column mean
mean = np.nanmean(arr, axis=0)


index = np.where(np.isnan(arr))

# Replace NaN
arr[index] = np.take(mean, index[1])

print(arr)
#Q4 Replace negative values with zero
import numpy as np

arr = np.array([2,-5,7,-9,4])

arr[arr < 0] = 0

print(arr)