import numpy as np

'''
numpy arrays are homogeneous, so all elements must be of same data type
cannot be like 'list', which ain't homogeneous
'''

lst = []
size = int(input("enter size: "))

for _ in range(size):
    x = int(input())
    lst.append(x)
    # lst.append(int(input()))

# print(lst) 

arr1 = np.array(lst)   # place the list in the object's place in array
print(arr1)