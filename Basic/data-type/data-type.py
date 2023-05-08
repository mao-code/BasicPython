# Numeric
# Int
x = 42
y = -10
z = 0

#Float
pi = 3.14
e = 2.71828
# ----------------------

# Boolean
is_raining = True
is_sunny = False
# ----------------------

# Sequence
# Str
name = "Alice"
message = 'Hello, world!'

# List
numbers = [1, 2, 3, 4]
names = ['Alice', 'Bob', 'Charlie']

# Accessing the element of a list (index)
print(numbers[2])

# slicing
# slicing is a way to extract a part of a sequence
# [start:end:step]
# [::] => create a copy of sequence
print(names[0:]) # index 0 to end
print(names[:2]) # index 0 to (2-1)
print(numbers[1:3]) # index 1 to (3-1)
print(names[-1]) # index count from the end


# Tuple
my_tuple = (1, 2, 3, 4)
# ----------------------

# Set 
my_set = {1, 2, 3, 4}
my_other_set = set([1, 2, 3, 4, 4])
# ----------------------

# Mapping
person = {
    'name': 'Alice', 
    'age': 25, 
    'city': 'New York'
}
# ----------------------