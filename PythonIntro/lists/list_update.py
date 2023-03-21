lst = [-1, 0, 2, 5, 7]
print("initial list:", lst)


# replace value at an index
lst[3] = 3
print("lst[3] = 3:", lst)


# insert n at nth index (without replacing)
lst.insert(2, 1)
print("insert(2, 1):", lst)


# insert values at [n:n]
lst[5:5] = [4, 5, 6]   # not including, index 5
print("lst[5:5] = [4, 5, 6]:", lst)


# append the list (at the tail)
lst.append(8)
print("append(8):", lst)


# extend the list (at the tail)
lst.extend([9, 10])
print("extend([9, 10]):", lst)