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
'''    

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