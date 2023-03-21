import numpy as np

'''
to find unique elements (using set()), first flatten the numpy array
then convert it into a set 
'''

A = np.array([[1, 2, 3, 4 ,5],
              [7, 8, 9, 7, 5],
              [9, 3, 2, 8, 5],
              [4, 2, 1, 7, 3]])  


# finding unique elements from each row
for i in range(len(A)):
    print(set(A[i].flatten()))
    

# find all unique elements
flat_array = A.flatten()   # flatten the array
print(set(flat_array))     # pass it in a set function