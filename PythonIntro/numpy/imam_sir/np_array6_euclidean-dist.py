import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 3, 5, 7, 2, 3])

x1 = 10
y1 = 20

# euclidean distance: (x-x1)**2 + (Y-Y1)**2

print(x - x1)
print(y - y1)

print(f"eulidean distance: {(x-x1)**2 + (y-y1)**2}")