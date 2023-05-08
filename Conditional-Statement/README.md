# Conditional Statement
Conditional statements are used in programming to execute different blocks of code depending on whether certain conditions are met.

# Logical operators
Logical operators are used in conditional statements to combine multiple conditions and produce a True or False result.

# If Statement
If statements check if a condition is True, and if so, they execute a block of code.

``` python
if condition:
    code to execute if condition is True
```

# If-else Statement
If-else statements check if a condition is True, and if so, they execute one block of code. If the condition is False, they execute a different block of code.

``` python
if condition:
    code to execute if condition is True
else:
    code to execute if condition is False
```

# If-else if Statement

``` python
if condition1:
    code to execute if condition1 is True
elif condition2:
    code to execute if condition1 is False and condition2 is True
...
else:
    code to execute if condition1, condition2, ... are all False
```

# Note
## if and if-elif
* if statement:
  * Checks if a single condition is true.
  * If the condition is true, the code block associated with the if statement is executed.
  * If the condition is false, the code block associated with the if statement is skipped.
  * Does not provide a way to check additional conditions if the first condition is false.
* if-elif statement:
    * Checks multiple conditions in a specific order.
    * If the first condition is true, the code block associated with that condition is executed and the rest of the if-elif statement is skipped.
    * If the first condition is false, the next condition is checked and the associated code block is executed if it is true.
    * The process continues until a condition is true or until all conditions have been checked.
    * Provides a way to check additional conditions if the first condition is false.

