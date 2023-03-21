''' make array using numpy '''
import numpy as np

# to make an empty 2-D array of 4/5 dimentions
arr1 = np.empty((4, 5))  # dimention is given, values ain't, so it stores garbage values
print(arr1)

print("-------------------------------")

# two 3/4 matrix
arr2 = np.empty((2, 3, 4))
print(arr2)

print("-------------------------------")

# two 3/4 matrix of value zero 
arr3 = np.zeros((2, 3, 4))
print(arr3) 

print("-------------------------------")

# arrays of ones
arr4 = np.ones((4, 5))
print(arr4)

print("-------------------------------")

# fill out with other element (7)
arr5 = np.full((2, 3), 7)
print(arr5)

print("-------------------------------")

# identity matrix
arr6 = np.identity(3)  # no need to pass both dimentions since it's square
print(arr6)   # 1s in diagonal