'''
Reading Files with Open

f1 = open('/sample_file.txt', 'w')

f1.name   # returns the name of the file object instance
f1.mode   # returns the mode of the file object instance

f1 = open('sample_file.txt', 'r')

f1_stuff = f1.read()
f1.close()   # closes the file

f1.closed   # checks to see if f1 is closed (returns true if closed)

try --> print(f1)
try --> print(f1_stuff)


with open('sample_file.txt', 'r') as f1:
    file_stuff_list = f1.readlines()
    file_stuff = f1.read()   # notice that this doesn't work; after the first
                             # line executes, the file is closed
    
print(file_stuff_list)
print(file_stuff)
print(file_stuff_list[0][1:3])

f2 = open('sample_file.txt', 'r')

f2_stuff = f2.read()
f2_stuff_list = f2.readlines()


print(type(f2_stuff))
print(type(f2_stuff_list))

print(f2_stuff)
print(f2_stuff_list)


f2.close()

with open('sample_file.txt', 'r') as f3:
    for line in f3:
        print(line)
        
with open('Example2.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    

Lines = ["This is line D\n", "This is line E\n", "This is line F\n"]

with open('Example2.txt', 'a') as writefile:
    for line in Lines:
        writefile.write(line)
        
with open('Example2.txt', 'r') as readfile:
    print(readfile.read())
    
with open('Example2.txt', 'r') as readfile:
    with open('Example3.txt', 'w') as writefile:
        for line in readfile:
            writefile.write(line)
            
with open('Example3.txt', 'r') as readfile:
    print(readfile.read())
'''

import pandas as pd

'''
csv_path = 'file1.csv'
df = pd.read_csv(csv_path)

xlsx_path = 'file1.xlsx'
df = pd.read_excel(xlsx_path)
'''

# you can cast a dictionary to a dataframe
songs = {'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon', \
                   'The Bodyguard', 'Bat Out of Hell'],
         'Released': [1982, 1980, 1973, 1980, 1977],
         'Claimed Sales': [65, 50, 45, 44, 42]}

songs_df = pd.DataFrame(songs)

print(songs_df)

songs_df1a = songs_df[['Album']]
print(type(songs_df1a))   # dataframe

songs_df1b = songs_df['Album']
print(type(songs_df1b))   # series

# dataframe slicing
songs_df1c = songs_df[['Album', 'Released']]
print(songs_df1c)

print(songs_df.iloc[0, 0])
print(songs_df.loc[0, 'Album'])

z1 = songs_df.iloc[0:2, [0,2]]
print(z1)

z2 = songs_df.loc[0:2, ['Album', 'Claimed Sales']]
print(z2)

z3 = songs_df.loc[0:3, 'Album':'Released']
print(z3)

# dataframe methods
unique_released_years = songs_df['Released'].unique()
print(unique_released_years)
print(type(unique_released_years))

# logical masking
modern_years = songs_df['Released'] >= 1980
modern_songs_df1 = songs_df[songs_df['Released'] >= 1980]
modern_songs_df2 = songs_df[modern_years]
print(modern_songs_df1)
print(modern_songs_df2)
print(type(modern_songs_df1))
print(type(modern_songs_df2))

songs_df.to_csv('songs.csv')