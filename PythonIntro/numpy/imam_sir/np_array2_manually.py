import numpy as np

# manually build-up an numpy array
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr1)

print("------------------------------------")

# array of different data type; explicit data type
arr2 = np.array([1.2, 3.4, 2, 4], dtype=float)
print(arr2)

print("------------------------------------")

# array from a range value

arr3 = np.arange(1, 100, 3)  # runs from 1 to 99 with 3 increment
print(arr3)

print("------------------------------------")

# make array of equidistant number in a range
arr4 = np.linspace(0, 1, 10)   # 10 equal division of numbers in the range
print(arr4)