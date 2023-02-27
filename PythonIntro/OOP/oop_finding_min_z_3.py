'''
create a vector class with 'x', 'y', and 'z' attributes
create a list of objects of the class, and assign values to x, y, z
from the list, find out the object holds the 'minimum z'
find the object's index and delete it
'''

from queue import PriorityQueue

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __lt__(self, other):
        return self.z < other.z



# creating obj(s) 
ob0 = Vector(1, 2, 4)
ob1 = Vector(1, 3, 5)
ob2 = Vector(4, 5, 2)
ob3 = Vector(1, 5, 1)
ob4 = Vector(9, 0, 3)

# list the objects
vec_lst = [ob0, ob1, ob2, ob3, ob4]

pq = PriorityQueue()

for i in range(len(vec_lst)):
    pq.put(vec_lst[i])

min_z = pq.get()
print(min_z.x, min_z.y, min_z.z)

# pq.remove()