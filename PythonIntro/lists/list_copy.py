print("--------------------------COPY LOCATION-------------------------------")

list1 = [1, 2, 3, 4, 6]
list2 = list1  # doesnt copy, rather refers to the same object

# changing one will affect another when both refer to the same obejct
list1[4] = 5

print("list1:", list1)
print("list2:", list2)

print("--------------------------COPY-------------------------------")

# to copy an attribute to another, 
listA = [10, 20, 30, 40]
listB = listA.copy()

# changing one will NOT affect another
listA[3] = 1000

print("listA:", listA)
print("listB:", listB)


print("--------------------------SHALLOW COPY-------------------------------")

listX = [1, 2, 3, 4, 5, [4, 20], 6, 7]
listY = listX.copy()

print("listX:", listX)
print("listY:", listY)

listX[0] = 0
listY[5][1] = 99

# since it's a shallow copy, list-within-the-list still referes to the same location 
print("listX:", listX)  # (0), 2, 3, 4, 5, [4, (99)], 6, 7
print("listY:", listY)  # (1), 2, 3, 4, 5, [4, (99)], 6, 7


listX = [1, 2, 3, 4, 5, [4, 20], 6, 7]
listY = listX.copy()


print("--------------------------DEEP COPY-------------------------------")

# for deepcopy, import copy module and use deepcopy()
# format: new_list = copy.deepcopy(your_list) 
import copy

listN = [1, 2, 3, 4, 5, [4, 20], 6, 7]
listM = copy.deepcopy(listN)

listN[0] = 0
listM[5][1] = 99

print("listN:", listN)  # (0), 2, 3, 4, 5, [4, (20)], 6, 7
print("listM:", listM)  # (1), 2, 3, 4, 5, [4, (99)], 6, 7