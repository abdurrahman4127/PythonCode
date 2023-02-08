class Employee:
    pass       # to leave empty for a time, use 'pass'

# creat instance of class  
emp1 = Employee()
emp2 = Employee()

# both have unique memory address
print(emp1)  
print(emp2)

# class instance initialization
emp1.first = "Abdur"
emp1.last = "Rahman"
emp1.email = "whoamiiammr.nobody@gmail.com"

emp2.first = "l"
emp2.last = "lawliet"
emp2.email = "llawliet@gmail.com"

print(emp1.email)
print(emp2.email)