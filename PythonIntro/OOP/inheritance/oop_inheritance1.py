class Parent:
    def __init__(self, name):
        self.parent_name = name    # instance variable of parent class
  
    # normal class method
    def print_parent(self):
        print(self.parent_name)

# in order to inherit a class, use ChildClass(ParentClass)
class Child(Parent):
    def __init__(self, c_name, p_name):
        
        # since we are extending parent class and it expects
        # a name argument, use super function to provide it 
        super().__init__(p_name)

        # instance variable of child class
        self.child_name = c_name   


    def print_child(self):
        print(self.child_name)
        print(self.parent_name)

# "nazmul" is passed to child's constructor to parent's constructor
ob1 = Child("AR", "Nazmul")    
ob1.print_child()