'''
Conditon Statements

==   equal
!=   not equal

logical tests on letters / words / sybmol use the associated ASCII integer 
  code as the basis for the test
  
If Statement (example)

age = 17
age_cutoff = 20
age_cutoff_str = str(age_cutoff)

if age > age_cutoff:
    print("You're older than " + age_cutoff_str)
elif age == age_cutoff:
    print("You're " + age_cutoff_str)
else:
    print("You're younger than " + str(age_cutoff_str))

print("This sentence will always appear")


Logical Operators

and
or
not
   

# List syntax version 1
squares = ['Red', 'Yellow', 'Green']

print(squares)

for i in range(0, len(squares)):
    squares[i] = 'white'

print(squares)
print('\n' * 3)
       
# List syntax version 2
squares = ['Red', 'Yellow', 'Green']

print(squares)

for i in squares:
    print(i)

print('\n' * 3)

# List enumeration
squares = ['Red', 'Yellow', 'Green']

for i, j in enumerate(squares):
    print(i)
    print(j)
    print('\n')
    
print('\n' * 3)

# While Loop Example
dates = [1982, 1980, 1973, 2000]

i = 0
year = []

while(dates[i] != 1973):
    year.append(dates[i])
    i = i + 1
    
print(year)


Functions

def add(a = 1):
    b = a + 1
    print(a, 'if you add one', b)
    return b
    
If there is no return statement, the function returns None.
Note in the function add, the argument has a default value of 1


# The function getBandRating below is good for understanding variable scope
def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)

def con(a, b):
    return(a + b)

# Observe the output of various invocations of the function con -->
con(1, 2)
con("A", "B")
con("A", 1)
con(["A", 1], ["B", 2])



Objects and Classes

Every object has 1) a type, 2) an internal data representation (a blueprint),
    and 3) a set of procedures for interacting with the object (methods)

An object is an instance of a particular type

type()   <-- used to find the type of an object

A class or type's methods are functions that every instance of that class
  or type provides. Methods are a means for interacting with the data in
  an object.
  
A Class has data attributes and methods

class Circle(object):
    
    def __init__(self, radius, color):
        self.radius = radius;
        self.color = color;
        
    def add_radius(self, r):
        self.radius = self.radius + r
        
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
       
once a class is defined, you can create (instantiate) objects of the class type
  for example, you can create an object of type Circle

C1 = Circle(4, "yellow")

print(C1.color)  
print(C1.radius) 

C1.color = 'red'   # this changes the color attribute of the C1 instance

print(C1.color)

C1.add_radius(4)

print(C1.radius)
 
 dir(Circle)
'''