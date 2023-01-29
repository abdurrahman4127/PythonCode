class MyClass:
    def __init__(self):
        self.instance_variable = "this is an instance variable"

    def print_varible(self):
        print(self.instance_variable)

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print("before changing: ")
obj1.print_varible()
obj2.print_varible()
obj3.print_varible()

# changing the value 
obj1.instance_variable = "changed obj1"

print("after making change through the obj1...")
obj1.print_varible()  # changes
obj2.print_varible()  # won't change the value since change was made for obj1 
obj3.print_varible()  # won't change the value since change was made for obj1

# to change the value for obj2 and obj3, change the instance variable's value
obj2.instance_variable = "new value"
obj3.instance_variable = "new value"

print("after making change through the obj2 and obj3...")
obj1.print_varible()    # no change
obj2.print_varible()    # new value
obj3.print_varible()    # new value

# to unshadow the value for obj1
del obj1.instance_variable   # deletes the 
'''
obj1 is no longer referencing any instance variable
so if obj1.print_varible() is called, it will raise an AttributeError 
because the attribute is undefined
'''

# obj1.print_varible()  # AttributeError 
'''
to prevent this, use class variable instead of instance variable 
and define it outside of the init method and initialize it with a value.
'''