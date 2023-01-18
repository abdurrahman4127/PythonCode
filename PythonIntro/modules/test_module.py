import module_file

print(module_file.var1)
print(module_file.func1())


# or using alias
import module_file as m

print(m.var1)
print(m.func1())

# var 2 isn't in the module, but in the file
var2 = "just a variable"

# dir(m) cannot find as it only looks into the module  
print(dir(m))   

# var2 can be found by dir() as it looks through everything used in this file
print(dir())