# variables inside the class are called instance variables

class MyClass:

    # self is an instance of the class
    def __init__(self):
        # when objects will be called, self = ob1 / ob2
        self.attribute1 = "value1"
        # more like ob.attribute

# compiler will automatically pass the self parameters
ob1 = MyClass()    # passes ob1 to 'self'
print("ob1.attribute1:", ob1.attribute1)