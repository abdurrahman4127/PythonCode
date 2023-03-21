'''
create a vector class with 'x', 'y', and 'z' attributes
create a list of objects of the class, and assign values to x, y, z
from the list, find out the object holds the 'minimum z'
find the object's index and delete it
'''

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # finding the index of the obj that holds the minimum z
    def min_z_index(self, vec_lst):
        self.minimum_z = 999999
        index = 0

        for i in range(len(vec_lst)):
            if vec_lst[i].z < self.minimum_z:
                self.minimum_z = vec_lst[i].z
                index = i
        
        return index

# creating obj(s) 
ob0 = Vector(1, 2, 4)
ob1 = Vector(1, 3, 5)
ob2 = Vector(4, 5, 2)
ob3 = Vector(1, 5, 1)
ob4 = Vector(9, 0, 3)

# list the objects
vec_lst = [ob0, ob1, ob2, ob3, ob4]

print("------------ before -------------")

for i in range(len(vec_lst)):
    print(f"ob{i}:", vec_lst[i].x, vec_lst[i].y, vec_lst[i].z)
print()

# finding the index of the obj that holds the minimum z
index = Vector.min_z_index(Vector, vec_lst)

deleted_obj = vec_lst[index]
print(f"deleting: [{deleted_obj.x}, {deleted_obj.y}, {deleted_obj.z}]")
del vec_lst[index]   # delete the object from the list
print()


print("------------ after -------------")
for i in range(len(vec_lst)):
    print(f"ob{i}:", vec_lst[i].x, vec_lst[i].y, vec_lst[i].z)