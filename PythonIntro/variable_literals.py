#  literals literally means constant (kinda)

# numeric literals
num1 = 0b1010   # 0b = binary
num2 = 10       # decimal    
num3 = 0o12     # 0o = octal
num4 = 0xA      # 0x = hexa-decimal

#gets auto-converted to decimal
print(num1, "| type:", type(num1)) # type of  num1-num4 are int 


# float/double literals: in python, float = double
float = 3.1416
float2 = 3.5e5

double = 3.1416
double2 = 3.5e5

print(float, float2, "| type:", type(float2))
print(double, double2, "| type:", type(double2))


# complex literals
comp = 3 + 4j
print("complex:", comp, "| type:", type(comp))     # complex number
print("real:", comp.real, "| type:", type(comp.real))   # .real to access real part
print("imag:", comp.imag, "| type:", type(comp.imag))   # .imag to access imaginary part
print("comp is an instance of complex:", isinstance(comp, complex))


# string literals
str1 = 'single qouted string'
str2 = "double qouted string"
str3 = '''multi-qouted 
    multi-line
    string'''

print(str1)
print(str2)
print(str3)


# boolean literals: seriously case-sensitive
print(0 == 0, "| type:", type(0 == 0)) # (T)rue, not '(t)rue'
print(0 == 1, "| type:", type(0 == 1)) # (F)alse, not '(f)alse'


# special literals: null
# (N)one = null; dont have null in python, use None
null = None
print(null, "| type:", type(null))