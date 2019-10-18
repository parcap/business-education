'''
Python Data Types

int      type(11)
float    type(21.213)
str      type('Hello Python 101')
bool     type(True)   type(False)

typecasting --> changing a variable from one type to another type
  float(2) <-- changes the integer 2 to a float 2.0
  int(1.1) <-- truncates the float 1.6 to an integer 1
  int('1') <-- changes the string '1' to an integer 1
  str(1.8) <-- changes float 1.8 to a string '1.8'
  int(True) <-- changes the boolean True to an integer 1
  int(False) <-- changes the boolean False to an integer 0
  bool(1) <-- changes the integer 1 to a boolean True
  bool(0) <-- changes the integer 0 to a boolean False


Python Expressions and Variables

Mathematical Operations --> 43 + 60 + 16 + 41 (operands and operators)
//  <-- integer division (i.e. decimal part of result is truncated)
**  <-- exponentiation
type(my_variable)  <-- returns the type of the variable my_variable


Python String Operations

It is helpful to think of a string as an ordered sequence.
Each element in the sequence can be accessed using an index
  represented by the array of numbers.
  
name = 'Michael Jackson'
name[0] --> "M"
name[5] --> "e"
name[-2] --> "o"
name[1:4] --> "ich"   <-- note that this does NOT include the 4th index
name[::2] --> "McalJcsn"
name[0:5:2] --> "Mca"

len(name) --> 15   <-- length of the string variable
name + " is the best!" --> "Michael Jackson is the best!"
3 * name --> Michael JacksonMichael JacksonMichael Jackson

Strings are IMMUTABLE (i.e. you can NOT change a specific index value)
  name[0] = "J"   <-- results in an error
  
\  <-- is an escape character
\n <-- new line --> name = "Michael Jackson \n is the best!"
\t <-- tab --> name = "Michael Jackson \t is the best!"
\\ <-- inserts a "\" character in the string

With strings you can apply sequence methods and string methods.
A = "Hello"   -->   B = A.upper()
A = "Michael Jackson"   -->   B = A.replace("Michael", "Janet")

name.find("el") --> 5
name.find("en") --> -1
'''