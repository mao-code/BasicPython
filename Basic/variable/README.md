# Python Variables

## Introduction
* Variables are used to store and manipulate data in a program
* Python is a high-level, dynamically-typed language, meaning that it can infer the data type of a variable based on the value assigned to it. 
* This makes it easy to write code quickly and easily, without worrying too much about data types or memory management.

## What are Variables in Python?
* Definition of a variable: 
  * A variable is a named location in memory that stores a value. 
  * The value can be of any data type (integer, float, string, boolean, etc.).
* Naming conventions for variables in Python: 
  * Variables in Python can be named using any combination of letters, digits, and underscores, but cannot start with a digit. 
  * By convention, variable names should be in lowercase and use underscores to separate words.
* Basic Data types in Python (int, float, string, boolean): Integers are whole numbers (e.g. 42), floats are decimal numbers (e.g. 3.14), strings are sequences of characters (e.g. "hello, world"), and booleans are either True or False.

## Declaring and Assigning Variables
* How to declare a variable in Python:
  *  To declare a variable in Python, you simply need to give it a name. For example, x could be a variable name.
* How to assign a value to a variable:
  *  To assign a value to a variable, you use the = operator. For example, x = 42 would assign the integer value 42 to the variable x.
* See more detail in code

## Variable Scope and Lifetime
* Scope of a variable: 
  * The scope of a variable refers to where it can be accessed in a program. In Python, <u>the scope of a variable is determined by where it is defined.</u>
* Local variables:
  *  Local variables are defined within a function or block of code, and can only be accessed within that function or block.
* Global variables:
  *  Global variables are defined outside of any function or block, and can be accessed from anywhere in the program.
* Lifetime of a variable: 
  * The lifetime of a variable refers to how long it exists in memory. 
  * Local variables are destroyed when the function or block of code they are defined in finishes executing
  * Global variables remain in memory until the program ends.