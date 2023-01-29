class MyClass:
    class_variable = "This is a class variable"
    
    def __init__(self, arg1):
        self.instance_variable = arg1
        
    def print_variables(self):
        print("Class variable:", MyClass.class_variable)
        print("Instance variable:", self.instance_variable)

obj1 = MyClass("Value 1")
obj2 = MyClass("Value 2")

obj1.print_variables()
obj2.print_variables()


print("------------------------------------------------------------------")

# trying to update the class variable on the obj1 object 
# obj1.class_variable = "class variable updated"   # but it doesn't exist there; error

MyClass.class_variable = "class variable updated"
obj1.instance_variable = "instance variable updated"

obj1.print_variables()
obj2.print_variables()  # instance variable for obj2 won't change