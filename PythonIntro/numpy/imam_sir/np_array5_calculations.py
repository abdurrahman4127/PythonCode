import numpy as np

''' element-wise operations '''

arr = np.array([[10, 20, 30], [40, 50, 60]])

# add n to each elements in the array
print(arr + 10)
print()

# subtrack n to each elements in the array
print(arr - 10)
print()

# multiply n to each elements; n * [[a, b, c],[x, y, z]]
print()


print("-------------------------------------")


# add two array
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([20, 40, 60, 80])

print(arr1 + arr2)