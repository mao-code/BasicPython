# Basic example of using the print() function
print("Hello, world!")

# Using variables and string formatting with the print() function
name = "Alice"
age = 25
print("My name is {} and I am {} years old".format(name, age))

# Specifying the separator and end character with the print() function
print("Item 1", "Item 2", "Item 3", sep="|", end="\n\n")
# ----------------------

# Basic example of using the input() function
name = input("What is your name? ")
print("Hello, {}".format(name))

# Using error handling with the input() function
try:
    age = int(input("What is your age? "))
except ValueError:
    print("Invalid input, please enter a number")
    age = 0
print("Your age is {}".format(age))
# ----------------------

# F-string
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")