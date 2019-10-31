# list comprehension approach
squares_lc = [x * x for x in range(10)]

# equivalent for-loop approach
squares_fl = []

for x in range(10):
    squares_fl.append(x * x)

# list comprehension with filtering criteria
even_squares_ls = [x * x for x in range(10) if x % 2 == 0]

# equivalent for-loop approach with filtering criteria
even_squares_fl = []

for x in range(10):
    if x % 2 == 0:
        even_squares_fl.append(x * x)

# good list comprehension formatting style
even_squares_lc_gf = [x * x
                      for x in range(10)
                      if x % 2 == 0]
        
print(squares_lc)
print(squares_fl)
print(even_squares_ls)
print(even_squares_fl)
print(even_squares_lc_gf)