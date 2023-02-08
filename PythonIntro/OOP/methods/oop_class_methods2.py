class MyClass:
    class_var = "version 1.0"
    
    # class method        
    @classmethod
    def change_class_variable(cls, new_value):
        cls.class_var = new_value


print("before updating...........")
before_updating = MyClass.class_var
print(before_updating)

print("after updating...........")
update = "version 1.1"
MyClass.change_class_variable(update)

after_updating = MyClass.class_var
print(after_updating)