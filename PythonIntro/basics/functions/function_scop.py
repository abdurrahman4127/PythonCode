# power-order (low -> high)
# function: local namespace
#   module: global namespace [if not found in local]
#       built-in namespace   [if not found in global]

g = 10      # global variable [built-in [global: g = 10 [local: ]]]

def f1():
    global g   
    g = 20     # refering to global variable g [built-in [global: g = 20 [local: ]]]

    # nl is local for f1(), non-local for f2()
    nl = 20  # [built-in [global: g = 20 [local: nl = 20]]]

    def f2():
        global g  # refering to global variable g
        g = 30  # [built-in [global: g = 30 [local: nl = 20 [local: ]]]]

        nonlocal nl  # refering to non-global variable nl of f1()
        nl = 30  # [built-in [global: g = 30 [local: nl = 30 [local: ]]]]

        l = 30   # local variable, l, for f2()
        print("l =", l)  # [built-in [global: g = 30 [local: nl = 30 [local: l=30]]]]
    
    f2()   # set g to 30, nl to 30 & print the value of l
    print("nl =", nl)  # print updated value of nl

f1()   
print("g =", g)