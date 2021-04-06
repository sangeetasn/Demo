# hello world prog
print("Hello, World!")
# conditional statement
if 5 > 2:
    print("Five is greater than two!")
# defining variables
x = 5;
y = 'Wali';
print(x)
print("Wali")
print(type(x))
print(type(y))
# variable names are case sensitive
a = 6;
A = "Sally"
print(a)
print(A)
# legal variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# illegal var names
# 5myvar"wali" SyntaxError: invalid syntax
# my-var='wali' SyntaxError: invalid syntax
# my var="wali" SyntaxError: invalid syntax
# Multi Words Variable Names
"""
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case

"""
myVariableName = "John"

# Pascal Case
MyVariableName = "John"

# snake case
my_variable_name = "John"

# assign Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assign One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables & concatenation ex1
x = "awesome"
print("Python is " + x)

# Output Variables & concatenation ex2
x = "python is "
y = "awesome"
z = x + y
print(z)

# Output Variables & concatenation ex3
# For numbers, the + character works as a mathematical operator:
y = 10
z = x + y
print(z)

# Output Variables & concatenation ex4
# If you try to combine a string and a number, Python will give you an error:
"""
x = 5
y = "John"
print(x + y)
"""

"""
Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""
x = "awesome"



