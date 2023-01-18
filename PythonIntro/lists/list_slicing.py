# array is of class list
a = [1, 2, 3, 4, 5, 6, 7] 
print(a)


# accessing in reverse order
print(f"a[-1] = {a[-1]}") # last 
print(f"a[-2] = {a[-2]}") # (last - 1) 
print(f"a[-3] = {a[-3]}") # (last - 2)


print(f"a[4:] = {a[4:]}")
print(f"a[:5] = {a[:5]}")
print(f"a[:] = {a[:]}")
print(f"a[0:] = {a[0:]}")
print(f"a[2:2] = {a[2:2]}")


# slicing the array
print(f"a[0:3] = {a[0:3]}")
print(f"a[2:7] = {a[2:7]}")
# print(f"a[2:8] = {a[2:8]}")
# print(f"a[2:9] = {a[2:9]}")

print(f"a[2:5] = {a[2:5]}")
print(f"a[3:6] = {a[3:6]}")

# to append; not to add
print(f"a[2:5] + a[3:6] = {a[2:5] + a[3:6]}")


# traversing with negative indexing:
# slicing only works from left -> right; not right -> left
print(f"a[-5:-1] = {a[-5:-1]}") 
# print(f"a[-1:-5] = {a[-1:-5]}") # this returns empty output