'''
class variable is a variable that is shared among all instances of a class. 
it is defined within the class, not outside of any of the class's methods, and
it works like static variables
'''

class MyClass:
    class_variable = "this is a class variable"
    
    def print_varible(self):
        print(self.class_variable)

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print("before changing: ")
obj1.print_varible()
obj2.print_varible()
obj3.print_varible()


# changing the value 
obj1.class_variable = "changed obj1"

print("after making change through the obj1...")
obj1.print_varible()  # changes
obj2.print_varible()  # won't change the value since change was made for obj1 
obj3.print_varible()  # won't change the value since change was made for obj1 


# to change the value for both, change the class variable's value
MyClass.class_variable = "new value"

print("after making change through the class...")
obj1.print_varible()    # no change; shadows the changes
obj2.print_varible()    # new value
obj3.print_varible()    # new value


'''
changing the value of MyClass.class_variable to "new value" wil updated all 
instances of the class that reference the class variable 
but since an instance variable was created in the previous step with the same name on obj1, 
it shadowed the class variable. so changing the value of MyClass.class_variable, won't affect 
the value of obj1's instance variable 
'''

# to retrive the value that got shadowed
del obj1.class_variable

print("after unshadowing...")
obj1.print_varible()    # new value
obj2.print_varible()    # new value
obj3.print_varible()    # new value