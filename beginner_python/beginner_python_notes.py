##Datacamp: Python Data Science Track

'''
Variables are useful for reproducibility. Allows you to refer to a value with a name.
The operator assignment in Python is '='
type(variable) ##returns class/type of the variable

int: integers (no decimal part)
float: numbers with decimal part
strings are used to store text
boolean (True/False)

How the code behaves depends on the data types

Summing two strings in python is equivalent to the paste0 operation in R

Python conversion functions:
	str() #To string
	bool() #To boolean
	int()  #To integer
	float() #To float
'''

'''
Lists

A list is a compound data type
Built with square brackets: []

list_type = [elements] ## name a collection of values. It may contain different data types

Lists can contain sub-lists as elements (list of lists)

Lists are subset using indices (0-indexed language)
Negative indices can be used (-1 indexed language)
list_name[element_number]

Syntax  for subsetting lists:  [start (inclusive): end (exclusive)]

								[:n] ##All elements from the first to n-1
								[n:] ##All elements from n to the end

Manipulating lists:

- Change list elements
- Element Manipulation
- To change multiple elements in a list: subset and then pass a new list with new values
- Concatenating lists can be done with the "+" operator


del(list[element_number]) ## Deletes element from list -> Element moves over one index

The difference between explicit and reference-based copies is subtle, but can be really important

'''

'''
Functions

Piece of reusable code to solve particular tasks

Functions require inputs to perform its calculations

sorted(list, reverse = True/False): to sort lists

Methods: Functions that belong to objects. They are called with the dot notation object.method(arguments)

Get indices from a list: list.index(element value)
Get	total count in a list: list.count(element value)

In Python, everything is an object and every object has methods associated with them, depending on type
Some methods change the object they work on 

list.reverse() ##Reverses the order of the elements in a list

'''

'''
Numpy


Mathematical operations over lists of values
Alternative to Python List: Numpy Array
	 - Calculations over entire arrays
	 - To create an array, pass a list of values
	 - Numpy arrays can contain only one type (similar to R vectors)
	 - Subsetting can be done like lists or passing an array of Booleans
	 	* When creating an array of Booleans, it is not necessary to pass brackets directly
	 - Arrays will force coercion of objects	


~Think of data frames as a list of arrays~

numpy array ~= R base vector

Python list ~= R list

First of all, numpy arrays cannot contain elements with different types.
If you try to build such a list, some of the elements' types are changed to end up with a homogeneous list. 
This is known as type coercion.


'''

'''
2-D Numpy Arrays
type(array) => numpy.ndarray

by creating multiple arrays, we can have an n-dimensional array

subsetting 2-d arrays:
	- if they have the same length, each list becomes a row, and each element becomes a column
	- To subset you have to follow the structure: array[row_index, column_index]

'''