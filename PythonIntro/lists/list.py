# by default, list works as stack in python 

# for array: array is basically list type object
arr = [1, 2, 3, 4, 5, 6, 7]
print("array:", arr)
print(f"length: {len(arr)}")
print("array is of type:", type(arr))


listA = ["python", "anaconda", 10]
print(listA)
print(listA[2]) # 2rd index -> 10


# list within a list
listB = ["python", "anaconda", [20, 30]]
print(listB)
print(f"length: {len(listB)}")
print(listB[2][1])  # 2nd index, 1st item = 30


# assign value to an index in the list
listB[2] = "black mamba" # this'll replace index 1's value
print(listB)


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