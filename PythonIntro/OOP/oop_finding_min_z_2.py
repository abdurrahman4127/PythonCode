class Vector:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __repr__(self):
    return f'({self.x}, {self.y}, {self.z})'

vec_list = [Vector(1,2,1), Vector(4,5,2), Vector(1,5,7), Vector(9,0,3), Vector(0,5,4)]


min_index = -1
min_z = 9999999

for i in range(len(vec_list)):
  if vec_list[i].z < min_z:
    min_z = vec_list[i].z
    min_index = i

print(vec_list)
min_vect = vec_list[min_index]

del vec_list[min_index]
print(vec_list)   # goes to the __repr__() function