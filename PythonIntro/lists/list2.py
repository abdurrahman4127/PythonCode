listA = [1, 2, 7, 3, 4, 5, 3, 6, 7, 2, 5]
print(listA)

# search for index: index (element)
print(listA.index(7))

# search for 'x' after 'y' index; index(x, y)
print(listA.index(7, 3))

# counts frequency of an element
findX = 7
# print(listA.count(findX))
print("frequency of {}: {}" .format(findX, listA.count(findX)))

# sort the list
listA.sort()
print(listA)

# print in reverse order
listA.reverse()
print(listA)

# remove duplicate elements; set contains NO duplicate values
print(set(listA))