"""
x = "awesome"

def myfunc():
  print("Python is: " + x)

myfunc()


"""

"""
If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will 
remain as it was, global and with the original value.
"""

"""
def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is: " + x)
"""

"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

"""
"""
x = "awesome"

def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)
"""
"""
Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

"""

#x = 5
#x = "Hello World"
#x = 20.5
#x = 1j
#x = ["apple", "banana", "cherry"]
#x = ("apple", "banana", "cherry")
#x = range(6)
#x = {"name" : "John", "age" : 36}
#x = {"apple", "banana", "cherry"}
#x = frozenset({"apple", "banana", "cherry"})
#x = True
#x = b"Hello"
#x = bytearray(5)
#x = memoryview(bytes(5))
print(type(x))
print(x)