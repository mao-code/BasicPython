# Nameing convention: lowercase and underscore

# Declare a variable
x = 42  # assign integer value 42 to variable x
pi = 3.14  # assign float value 3.14 to variable pi
name = "Alice"  # assign string value "Alice" to variable name
is_true = True  # assign boolean value True to variable is_true
# ----------------------

# Example code for dynamically-typed variables
x = 42  # integer variable
x = 3.14  # now a float variable!
# ----------------------

# Example code for variable scope and lifetime
x = 42  # global variable

def my_function():
    y = 3.14  # local variable
    print(x)  # can access global variable from within function
    print(y)  # can access local variable from within function

my_function()
print(x)  # can access global variable from outside function
print(y)  # will throw a NameError, since y is only defined within my_function()