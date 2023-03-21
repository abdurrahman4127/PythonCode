import numpy as np

a = np.array([[1, 2, 3, 4 ,5],
              [7, 8, 9, 7, 5],
              [9, 3, 2, 8, 5],
              [4, 2, 1, 7, 3]])           

# find the maximum element in the array
print("max:", a.max())

# finding maximum
print(a.max(axis = 0))  # column-wise
print(a.max(axis = 1))  # row-wise


print()

# indices of the maxs
print(a.argmax(axis = 0))  # column-wise
print(a.argmax(axis = 1))  # row-wise


'''
get middle elements
 
1, 2, 3, 4 ,5
7, [8, 9, 7], 5
9, [3, 2, 8], 5
4, 2, 1, 7, 3
'''


lst1 = a[1][1:4]
lst2 = a[2][1:4]
print("lst1:", lst1)
print("lst2:", lst2)

a_new = np.array([lst1, lst2])
print(a_new)

print(a_new.shape)