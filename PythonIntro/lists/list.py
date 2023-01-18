# for array: array is basically list type object
arr = [1, 2, 3, 4, 5, 6, 7]
print("array:", arr)
print(f"length: {len(arr)}")
print("array is of type:", type(arr))


# remove element
arr.remove(2)
arr.remove(4)
arr.remove(6)
print(arr)


# clear the list: delete the list entirely
arr.clear()
print("after clearing:", arr)


listA = ["python", "anaconda", 10]
print(listA)
print(listA[2]) # 3rd index -> 10


# list within a list
listB = ["python", "anaconda", [20, 30]]
print(listB)
print(listB[2][1])  # 3nd index, 2st item -> 30


# remove 20
listB[2].remove(20)
# listB[2].pop(listB[2].index(20))
print(listB)


# assign value to an index in the list
listB[2] = "black mamba" # this'll replace index 1's value
print(listB)
print(f"length: {len(listB)}")   # 3


# insert into the list (doesn't replace)
listB.insert(2, "viper")
print(listB)


# to add at the tail, use append 
listB.append("king cobra")
print(listB)


# appending listA into listB
# listB.append(listA)
# print(listB)


# search in the list
if 'anaconda' in listA:
    print("yeah, anaconda is in the listA")
if "anaconda" in arr:
    print("yeah, anaconda is in the array")
else:
    print("no, anaconda not in the array")