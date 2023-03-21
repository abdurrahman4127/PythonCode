import numpy as np

a = np.array([[1, 2, 3],
                [4, 5, 6]])

b = np.array([[0, 2, 1],
                [4, 0, 3]])

# to check dimention (i.e. shape)
a_row, a_col = a.shape
print("row:", a_row)
print("col:", a_col)


# perform matrix addition
addition = a + b
print(addition)