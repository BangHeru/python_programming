"""
The Python Command Line

    (venv) p$[17:13:56]> python.exe 
    
The way to run a python file is like this on the command line:
    python.exe .\hello_world.py 


Python Indentation
Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
Python uses indentation to indicate a block of code.

"""
# Contoh yang benar :
if 5 > 2:
  print("Five is greater than two!")
  
# Contoh yang salah :
if 5 > 2:
print("Five is greater than two!")
  

# Ini juga contoh yang benar
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
        
# Yang ini contoh yang salah
# You have to use the same number of spaces in the same block of code, 
# otherwise Python will give you an error:

if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")


"""
Exercise

Insert the missing part of the code below to output "Hello World".

 ___ ("Hello World")
"""

# Insert the missing indentation to make the code correct:
"""
if 5 > 2:
print("Five is greater than two!")
"""
