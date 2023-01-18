# by default, list works as stack in python 

listA = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(listA)


# delete: provide index (not value)
del listA[0]
print("del listA[0]:", listA)    # [20, 30, 40, 50, 60, 70, 80, 90, 100]


del listA[3:6]
print("del listA[3:6]:", listA)    # [20, 30, 40, 80, 90, 100]


# remove: provide the value (not index); search the list & remove specific element
listA.remove(20)  
print("remove(20):", listA)    # [30, 40, 50, 60, 70]


# pop() pops the last element, like stack
listA.pop()
print("pop():", listA)


# clear: cleans out the whole list. list exists, value doesn't
listA.clear()
print("clear():", listA)


# delete the entire existence of of the list
del listA
# print(listA) # this'll output error since listA doesn't exist 