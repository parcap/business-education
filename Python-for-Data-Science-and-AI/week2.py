'''
Tuples

Tuples are an ordered sequence.
Tuples are written as comma-separated elements within parentheses.
ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
tuple1 = ("disco", 10, 1.2)

type(tuple1) --> tuple

tuple1[0] --> "disco"
tuple1[1] --> 10
tuple1[2] --> 1.2
tuple1[-1] --> 1.2

tuple2 = ("hard rock", 10)
tuple3 = tuple1 + tuple2

tuple3 --> ("disco", 10, 1.2, "hard rock", 10)

tuple3[1:3] --> (10, 1.2)
len(tuple3) --> 5

Tuples are IMMUTABLE
tuple3[2] = 1.4   <-- this generates an error

ratings_sorted = sorted(ratings)

ratings_sorted --> (2, 5, 6, 6, 8, 9, 9, 10, 10)

nested_tuple = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))

nested_tuple[2] --> ("pop", "rock")
nested_tuple[2][0] --> "pop"
nested_tuple[2][0][1] --> "o"
nested_tuple[4][1][1] --> 2

tuple1.index(10)


Lists

Lists are also ordered sequences.
Lists are written as comma-separated elemnts within square brackets.
Unlike tuples, lists are MUTABLE.

list1 = ["Michael Jackson", 10.1, 1982, (12, 13, "alpha")]
list1[0] --> "Michael Jackson"
list1[0][2] --> "c"
list1[-1] --> (12, 13, "alpha")
list1[2:4] --> [1982, (12, 13, "alpha")]   <-- this outputs a list

list2 = ["Hello", 2]
list3 = list1 + list2

list3 --> ["Michael Jackson", 10.1, 1982, (12, 13, "alpha"), "Hello", 2]

list4 = ["Hello", "there"]
list4.extend(["How", "are", 3])  <-- use extend carefully!!

list4 --> ["Hello", "there", "How", "are", 3]
len(list4) --> 5

list5 = ["Hello", "there"]
list5.append(["How", "are", 3])

list5 --> ["Hello", "there", ["How", "are", 3]]
len(list5) --> 3

list5[2]  = "Phil"   <-- demonstration of how lists are immutable
list5 --> ["Hello", "there", "Phil"]

del(list5[1])   <-- deletes the elements in index 1

Convert a string to a list
s1 = "hard rock"
s1_list = s1.split()   <-- space is the delimiter

s2 = "A, B, C, D"
s2_list = s2.split(",")   <-- comma is the delimiter

Aliasing
A = ["hard rock", 10, 1.2]
B = A   <-- in this case both A and B are referencing the same list
B = A[:}   <-- in this case B is a cloned version of A
               and therefore are not referencing the same list
               
help(A)   <-- gets help of the object in parentheses


Dictionaries

Dictionaries are denoted by { }
The keys have to be unique and are IMMUTABLE
The values can be immutable, mutable, and duplicates
Each key-value pair is separated by a comma

websters = {"A": 1, "B": "2", "C": [3, 3, 3], "D": (4, 4, 4), "E": 5, "F": 6}

websters["D"] = (4, 4, 4)
websets["G"] = ["Hello", "there!"]   <-- adds a new entry to the dictionary
del(websters["E"])   <-- deletes the row indexed by "E"
"F" in websters   <-- checks if index is in dict
websters.keys()   <-- generates a dict_list of all index entries
websters.values()   <-- generates a dict_values of all values entries
'''