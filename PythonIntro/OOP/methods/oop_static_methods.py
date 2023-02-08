'''
>   defined inside a class
>   doesn't have any reference to the instance or class of the object
>   don't need to create an instance of the class in order to access
>   class variable works like static variable; but
    class methods and static methods are different
'''

class MyClass:
    
    # default constructor
    def __init__(self, name):
        self.name = name
    
    # doesn't have 'self' key
    @staticmethod
    def static_method(arg):
        return arg**2
    

num = int(input("enter a number: "))
square = MyClass.static_method(num)

print(square)