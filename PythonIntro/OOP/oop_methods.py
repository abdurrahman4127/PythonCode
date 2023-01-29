class MyClass:
    def __init__(self, first, last):
        self.fname = first
        self.lname = last

    # 'self' is by default
    def print_name(self):
        print(f"full name: {self.fname} {self.lname}")

# taking inputs
first_name = input("enter first name: ")
last_name = input("enter last name: ")

# initializing the obejcts with values
obj = MyClass(first_name, last_name)

# print with the 'print_name()' method
obj.print_name()

# alternative way; not recommended
MyClass.print_name(obj)