"""
PEP 8

Guidelines and best practices for writing Python

Zen of Python
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

Useful when revisiting old projects

Helps in a collaborative setting
"""

# NAMING CONVENTIONS
def my_function():
    pass

x = 2
my_variable = "two"

#constant
GRAVITY_ACCELERATION = 9.81

class CoolCat():
    def my_method():
        pass

""" my_module.py   <-- module naming convention """

# don't use single letters for string variables
full_name = 'John Smith'   

first_name, last_name = full_name.split()

def multiply_by_two(x):
    return x * 2

multiply_by_two(5)


# CODE LAYOUT
# separate classes by two blank lines
# separate functions and methods by a single blank line
# use a blank line with code to compartmentalize ideas
# do NOT put too many blank lines as this will impair readability

class MyFirstClass():
    def first_method(self):
        pass
    
    def second_method(self):
        pass


class MySecondClass():
    pass


def top_level_function():
    pass

# Maximum Line Length
# you should limit maximum line length to 79 characters
# use implied continuation
def my_function(arg_one, arg_two,
                arg_three, arg_four):
    return arg_one

# use \ to force line continuation (implied continuation is preferred)
"""
from mypkg import example1, \
    example2, example3
    
total = (first_variable
         + second_variable
         - third_variable)
"""

# INDENTATION
# identation after implied continuation
def my_function(
        arg_one, arg_two,
        arg_three, arg_four):
    return arg_one

if (x > 3 and
        x < 10):
    print(x)
    
list_of_numbers = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
        ]


# COMMENTS
# block comments
for i in range(0, 10):
    # loop over i ten times and print out the value of i,
    # followed by a new line character
    print(i, "\n")

def quadratic(a, b, c, x):
    # Calculate the solution to a quadratic equation using the 
    # quadratic formula
    # 
    # There are always two solutions to a quadratic equation,
    # x_1 and x_2
    x_1 = (- b+(b**2-4*a*c)**(1/2))
    x_2 = (- b-(b**2-4*a*c)**(1/2))
    return x_1, x_2

# inline comment
x = 5  # this is an inline comment (although try not to use too many of these)

# doc strings
# single or multiline doc strings are embedded throughout this script


# WHITESPACE IN EXPRESSIONS AND STATEMENTS
def my_function(default_param=5):
    pass

# single operators
x = 5
y = 0
y += 1
x == y
x != y
x is None
y not in lst
x and y
True or False

# multiple operators
y = x**2 + 5
x = (x+y) * (x-y)

if x>5 and x%2==0:
    print('something')

# slicing and multiple parameters
my_list[1:2]
my_list[x+1 : x+2]
my_list[x+1 : x+2 : x+3]
my_list[x+1 : x+2 :]

my_tuple(3,)

print(x, y)


# PROGRAMMING RECOMMENDATIONS
greater_than = 6 > 5
if greater_than:
    return "6 is greater than 5"

my_list = []
if not len(my_list):
    print("List is empty!")
    
my_list = []
if not my_list:
    print("List is empty!")
    
# the example using my_list works because of truthy / falsy property
# truthy / falsy means a variable is considered true / false without
# explicitly being set to True or False

if not x is None:
    # this isn't as readable as the version below
    return "x is set to a value"

if x is not None:
    return "x is set to a value"

def my_function(my_param=None):
    if param is not None:
        print("my_param has some non-None value")

# think about methods over list slicing
if word[:3] == "cat":
    return "word starts with cat"

# this is a better implementation
if word.startswith("cat"):
    return "word starts with cat"

# methods are super helpful in testing endswith
if file.endswith(".jpg"):
    return "file is a jpg"

# pip install pycodestyle
# pycodestyle my_script.py

# pip install flake8
# flake8 my_script.py

# pip install black
# black --line-length=79 my_script.py

