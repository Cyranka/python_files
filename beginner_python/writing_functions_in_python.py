'''
Docstring is a string that is usually the first line of a function
It is used for description purposes
'''

def the_answer()
	"""
	This functions does something
	"""

print(the_answer.__doc__) ##Return the doc strings of the answer function

inspect.getdoc(function_name)
'''
Code 1: Doc strings example

'''

def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  Returns:
    int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])

'''
Using context managers
Context managers:

* Set up a context (environment where code runs)
* Run your code
* Remove the context (close)

with <context-manager>(<args>):
	#Run code here
	#this code is running inside a context

'''

'''
Code 1: Context Managers
'''

# Open "alice.txt" and assign the file to "file"
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split(): ##Splitting textt
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

'''

Writing context managers

Dumbified explanation: run arguments, yield values, then finish something 
1. Define a function
2. Add any set up code your context needs
3. Use the yield keyword
4. Add any teardown code
5. Add the @contextlib.contextmanager decorator in the line immediately above the function
'''

'''
Code 2: Additional Context Managers
'''

@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())


'''
Advanced Topics: Nesting contexts

with open(src) as f_src:
  with open(dst,'w') as f_dst:
    for line in f_src:
      f_dst.write(line)

Context manager patterns:
Open - Close
Lock - Release
Change - Reset
Enter - Exit
Start - Stop
Setup - Teardown
Connect - Disconnect      
'''

'''
Code 3: Nested Context Managers
'''

# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open('NVDA.txt','w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))


'''
Functions are objects:

* Functions are variables
x = my_function #Do not use parentheses, because them you would be calling the function, so the output gets assigned
x()

* Functions can also be wrapped into lists
list_of_functions = [my_function, open, print]

* Functions can be passed as inputs

def has_docstrings(func):
  """
  Some text
  """

  return func.__doc__ is not None

* Functions can be defined within other functions (nested)   
'''

'''
Code 4: Building a dictionary of functions and referencing them

'''
# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)


'''
Code 5: Using functions as inputs
'''

# Call has_docstring() on the log_product() function
ok = has_docstring(log_product) ##Notice that when using functions as inputs, we don't use ()

if not ok:
  print("log_product() doesn't have a docstring!")
else:
  print("log_product() looks ok")


'''
Code 6: Defining functions within functions and returning a function from a function
'''

def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b
    return add
  elif func_name == 'subtract':
    # Define the subtract() function
    def subtract(a,b):
      return a - b
    return subtract
  else:
    print("I don't know that one")
    
add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))


'''
Scope: Which variables can be accessed at different points in your code

Scope rules:
- Local
- Nonlocal (scope of a parent function, if it exists)
- Global
- Builtins

x = 7
def foo():
  global x ##This will call the 'global' x defined outside the scope of the function
  x = 42    ##Now we reassign the value 42 to the global x
  print(x)


'''

'''
Code 7: Local functions

'''

x = 50

def one():
    x = 10

def two():
  global x
  x = 30    

def three():
    x = 100
    print(x)
    
for func in [one, two, three]:
    func()    ##Call the function
    print(x)
'''
one() doesn't change the global x, so the first print() statement prints 50.
two() does change the global x so the second print() statement prints 30.
The print() statement inside the function three() is referencing the x value that is local to three(), so it prints 100.
But three() does not change the global x value so the last print() statement prints 30 again.
'''

'''
Code 8: Closures
Accessing values in a closure
* Defintions
  * Nested function: a function defined inside another function
  * Closure: nonlocal variables attached to a returned function

'''

def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])

'''
You can modify, delete, or overwrite the values needed by the nested function,
but the nested function can still access those values because they are stored safely in the function's closure
'''

'''
Decorators: a wrapper around a function that changes the function's behaviors

def multiply(a,b):
  return a*b

def double_args(func):
  #define a new function to modify the input
  def wrapper(a,b):
    return func(2*a,2*b) ##Takes two arguments and pass them to the input function

  return wrapper  

new_multiply = double_args(multiply)
new_multiply(1,5)

'''

'''
Code 9: Calling decorators
'''

# Decorate my_function() with the print_args() decorator
@print_args
def my_function(a, b, c):
  print(a + b + c)

my_function(1, 2, 3)


'''
Decorators (Part 2)
Whenn to use: Add common behavior to multiple functions
'''

'''
Code 10: Creating a basic decorator
'''

def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))


'''
Code 11: Counter decorator
'''

def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func(*args, **kwargs)
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))

'''
Decorators and metadata

from functools import wraps
@wraps(func)

function.__wrapped__

Think of decorators as a way to wrap functions with similar arguments.
'''

'''
Code 12: Using function wrappers
Notice how the decorator works. It defines a nested function and returns a nested function
'''

from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)


'''
Code 13: Obtaining the values of the nested function
'''

@check_everything
def duplicate(my_list):
  """Return a new list that repeats the input twice"""
  return my_list + my_list

t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))

'''
To add arguments to decorators, we need to add another level of function nesting
A decorator is a function that takes a function as an argument

def run_n_times(n):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator      
'''

'''
Example of real world decorator: timeout()
'''

################################################################################
'''
Extra code (EC)
'''

'''
EC 1: Calculating the median
'''

def median(values):
  """Get the median of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the median() function
  midpoint = int(len(values)/2)
  if len(values)%2 ==0:
    median = (values[midpoint -1] + values[midpoint])/2
  else:
    median = values[midpoint]
  return median


'''
EC 2: Finding default arguments

from functools import wraps
@wraps(func)

function.__wrapped__
'''

function.__name__ ##return function name

function.__defaults__ ##return function arguments

function.__doc__ ##returns function doc strings