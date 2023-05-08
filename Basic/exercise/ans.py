# 1. reverse a string (no loop)
""" 
String Sliceing 
1. [::-1] 
=> copy original string and step with -1
=> start from the end of the string and move backwards with a step size of -1

2. reverse()
You can also use the built-in reversed() function to 
reverse the string, but it will return a reversed iterator object 
that needs to be converted back to a string using the join() 
note: join() is a string method that concatenates a sequence of strings
"""

str = input("Please input a string: ")
print(str[::-1])
print(''.join(reversed(str)))

# 2. 
numbers = input("Enter a list of integers, separated by spaces: ").split()

# convert the input values to integers
numbers = list(map(int, numbers))

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

# 3.
sentence = input("Enter a sentence: ")
words = sentence.split()
num_words = len(words)
print(num_words)

# 4.
list1 = input("Enter list1 of integers, separated by spaces: ").split()
list2 = input("Enter list2 of integers, separated by spaces: ").split()

list1 = list(map(int, list1))
list2 = list(map(int, list2))

common_list = list(set(list1) & set(list2))
print(common_list)