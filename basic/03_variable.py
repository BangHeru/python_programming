"""
Creating Variables

Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.


"""

x = 5
y = "John"
print(x)
print(y)

"""
Variables do not need to be declared with any particular type and can even change
type after they have been set.
"""

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'


"""
Variable Names
A variable can have a short name (like x and y) or a more 
descriptive name (age, carname, total_volume). 
Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and 
       underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)

"""


"""
Assign Value to Multiple Variables
Python allows you to assign values to multiple variables in one line:
"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)


"""
Output Variables
The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:
"""

x = "awesome"
print("Python is " + x)

# You can also use the + character to add a variable to another variable:
x = "Python is "
y = "awesome"
z =  x + y
print(z)

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# If you try to combine a string and a number, Python will give you an error:
x = 5
y = "John"
print(x + y)



"""
Global Variables
Variables that are created outside of a function (as in all of the examples above) are 
known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# If you create a variable with the same name inside a function, 
# this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, 
# global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, 
and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.
"""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, 
# refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

