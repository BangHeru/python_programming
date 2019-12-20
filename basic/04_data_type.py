"""
Python Data Types

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


# Getting the Data Type
# You can get the data type of any object by using the type() function:
x = 5
print(type(x))

# hasil : <class 'int'>

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

x = "Hello World"                   # tipe data string / str
x = 20                              # tipe data integer / int
x = 20.5                            # tipe data float
x = 1j                              # tipe data complex
x = ["apple", "banana", "cherry"]   # tipe data list
x = ("apple", "banana", "cherry")	# tipe data tuple	
x = range(6)	                    # tipe data range	
x = {"name" : "John", "age" : 36}	# tipe data dict	
x = {"apple", "banana", "cherry"}	# tipe data set	
x = frozenset({"apple", "banana", "cherry"})	# tipe data frozenset	
x = True	                        # tipe data bool	
x = b"Hello"	                    # tipe data bytes	
x = bytearray(5)	                # tipe data bytearray	
x = memoryview(bytes(5))	        # tipe data memoryview


"""
Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:
"""

x = str("Hello World")	                        # str	
x = int(20)	                                    # int	
x = float(20.5)	                                # float	
x = complex(1j)	                                # complex	
x = list(("apple", "banana", "cherry"))	        # list	
x = tuple(("apple", "banana", "cherry"))	    # tuple	
x = range(6)	                                # range	
x = dict(name="John", age=36)	                # dict	
x = set(("apple", "banana", "cherry"))	        # set	
x = frozenset(("apple", "banana", "cherry"))    # frozenset	
x = bool(5)	                                    # bool	
x = bytes(5)	                                # bytes	
x = bytearray(5)	                            # bytearray	
x = memoryview(bytes(5))	                    # memoryview



