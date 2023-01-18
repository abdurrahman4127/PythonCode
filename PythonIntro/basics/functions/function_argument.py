#  function argument
def show_info(name, id, mail):
    print("name: {}".format(name))
    print("ID: {}".format(id))
    print("mail: {}".format(mail))
    print()

show_info("l lawliet", "123", "l@gmail.com")

# --------------------------------------------------

# keyword argument
def show_info2(name, id, mail):
    print("name: {}".format(name))
    print("ID: {}".format(id))
    print("mail: {}".format(mail))
    print()

# if keyword is uded, arguments can be passed in any order
show_info2(id="123", name="l lawliet", mail= "l@gmail.com")

# --------------------------------------------------


# default arguments have to be at the end of the argument list 
# def show_info3(name = "l lawliwt", id, mail):  # error
def show_info3(mail, name = "l lawliwt", id="1234"):
    print("name: {}".format(name))
    print("ID: {}".format(id))
    print("mail: {}".format(mail))
    print()

# if keyword is used, arguments can be passed in any order
show_info3(mail= "l@gmail.com")


