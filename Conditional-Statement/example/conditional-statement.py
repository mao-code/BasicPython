# logical operator
print(2>10 and 3<4)
print(True or False)

# if statement
# Example 1
x = 5
if x > 0:
    print("x is positive")

# Example 2
password = input("Enter your password: ")
if password == "secret":
    print("Access granted")

# Example 3
length = 10
width = 5
if length > 0 and width > 0:
    area = length * width
    print("The area of the rectangle is", area)

#if-else statement
# Example 1
x = 5
if x > 0:
    print("x is positive")
else:
    print("x is not positive")

# Example 2
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 3
num = 7
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# if-else if statement
num = 3

if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Number not found")