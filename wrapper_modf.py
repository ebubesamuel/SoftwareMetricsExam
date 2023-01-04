from math import modf

def wrapper(argument1):
    if not(isinstance(argument1, float)):
        msg = "argument must be a float, given argument is"+ str(type(argument1))
        raise TypeError(msg)
    return modf(float(argument1))

#in ordeer to test the cases, input in the assert wrapper below a different type eg. int/str
assert wrapper(1.79)
print(wrapper(1.79))
