''' class methods: used for constructor overloading '''

class MyClass:
    cls_var = 10

    # default constructor
    def __init__(self, name):
        self.name = name
    
    # normal method: recieves instance of the class by default
    def normal_method(self):
        print(self.name)

    
    @classmethod   # recieves the class
    def mycls_method(cls, name):      # it's more like: mycls_method(cls=MyClass, name):
        # it returns: return MyClass(name)
        return cls(name)   # returns a class object


    # to update the class variable
    @classmethod
    def mycls_update_var(cls):
        cls.cls_var = 20


# ob1 is built-up by '__init__()' 
ob1 = MyClass('abdur rahman')   

# class method gets called by class name
ob2 = MyClass.mycls_method('l lawliet')
    
ob1.normal_method()
ob2.normal_method()

print("checking if the class variable is updated................")

print("before updating....")
before = MyClass.cls_var
print("cls_var =", before)

print("after updating....")
MyClass.mycls_update_var()   # update through the class
after = MyClass.cls_var    
print("cls_var =", after)