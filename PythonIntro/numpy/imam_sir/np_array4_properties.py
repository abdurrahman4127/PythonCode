import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])
print(arr)
print(f"size: {arr.size}")
print(f"dimention: {arr.ndim}")  
print(f"shape: {arr.shape}") 
print(f"type: {type(arr)}")
print(f"data type: {arr.dtype}") 

# transpose the array
print(arr.T) 