class MyClass:

    # recieving parameters in the constructors
    def __init__(self, val1, val2):
        self.first = val1
        self.last = val2

# taking inputs
first_name = input("enter first name: ")
last_name = input("enter last name: ")

# initializing the obejcts with values
obj = MyClass(first_name, last_name)

print(f"full name: {obj.first} {obj.last}")