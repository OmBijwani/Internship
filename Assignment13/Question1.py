import numpy as np

arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])

arr = np.nan_to_num(arr, nan=0)

print("After replacing NaN:")
print(arr)

arr_transpose = arr.T

print("\nAfter interchanging rows and columns:")
print(arr_transpose)