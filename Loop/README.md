# Loop
Introduction to Loops:

Loops are used to repeatedly execute a block of code based on a condition.
They allow automating repetitive tasks and iterating over sequences or ranges.
Types of loops in Python: for loop and while loop.

---

# for-loop

(in python => iterate a sequence or range()) </br>
syntax: 
``` python
for item in sequence:
    # code to be executed
```

# while-loop

syntax: 
``` python
while condition:
    # code to be executed
```

Infinite loops and loop termination:
``` python
while True:
    # code to be executed
    if condition:
        break  # terminate the loop
```

---

# Looping Techniques:
* enumerate() function: Iterates over a sequence and provides the index and value of each item.
* zip() function: Iterates over multiple sequences simultaneously.
* range() function: Generates a sequence of numbers.
* Looping with multiple lists: Iterates over multiple lists together using zip().
* Looping with dictionaries: Iterates over keys, values, or key-value pairs of a dictionary.