import numpy as np

'''number of columns of the first matrix (A) must match the number of rows
of the second matrix (B) in order for matrix multiplication to be valid.'''


# to check if multiplication is possible 
def matrix_multiplication(A, B):
    A_row, A_col = A.shape
    B_row, B_col = B.shape
    
    if A_col == B_row:
        print(A.dot(B))
    else:
        print("col of 1st array has to be same as row of 2nd array")
        

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[0, 2, 1], [4, 0, 3], [2, 9, 5]])
matrix_multiplication(A, B)
# to multiply matrix