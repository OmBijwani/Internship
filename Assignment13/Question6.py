import numpy as np

A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])

B = np.array([9, -6, 17])

solution = np.linalg.solve(A, B)

print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])