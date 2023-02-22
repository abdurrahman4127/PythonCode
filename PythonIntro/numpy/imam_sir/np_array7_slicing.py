import numpy as np

''' format: [start : end : increment] '''

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])
print(arr[1:-1:2])
print(arr[1:-1:1])
print(arr[::3])