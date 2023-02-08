import numpy as np

a = np.array([[1, 2, 3, 4 ,5],
              [7, 8, 9, 7, 5],
              [9, 3, 2, 8, 5],
              [4, 2, 1, 7, 3]])           

print(a[1][4])
print(a[0:, 1:3])

# find the maximum element in the array
print("max:", a.max())


# finding maximum
print(a.max(axis = 0))  # column-wise
print(a.max(axis = 1))  # row-wise

# indices of the maxs
a.argmax(axis = 0)  # column-wise
a.argmax(axis = 1)  # row-wise