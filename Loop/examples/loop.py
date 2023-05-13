# Iterating over a sequence: (foreach)
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# Iterating over a range of numbers: (for)
for i in range(1, 5):
    print(i)

# break and continue statement
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  # exit the loop
    if num == 2:
        continue  # skip this iteration
    print(num)

# Nested for loops:
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

# ----

# Condition-based while looping:
count = 0
while count < 5:
    print(count)
    count += 1

# ----
# Looping techniques

# enumerate(): 
# It allows you to iterate over a sequence while also keeping track 
# of the index or position of each element.
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(index, fruit)

# zip(): 
# It combines multiple iterables (lists, tuples, etc.) into a single iterator, 
# pairing the corresponding elements from each iterable.
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

for num, letter in zip(numbers, letters):
    print(num, letter)


# range(): It generates a sequence of numbers within a specified range.
# Print even numbers from 2 to 10
for num in range(2, 11, 2):
    print(num)