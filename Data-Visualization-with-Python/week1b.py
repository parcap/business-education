'''
matplotlib -- Plot Function

pandas has a built-in implementation of matplotlib
  therefore, plotting in pandas is as simple as calling the plot
  function on a give pandas series or dataframe
  
plt.show()   <-- find out exactly what this method does
'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

plt.plot(5, 5, 'o')

india_china_df = pd.read_csv('india_china_data.csv', index_col = 0)
plt.show()

india_china_df.plot(kind = 'line')
plt.show()

india_china_df['India'].plot(kind = 'hist')
plt.show()

df_can = pd.read_excel(
            'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-' \
            'data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
            sheetname = 'Canada by Citizenship',
            skiprows = range(20),
            skip_footer = 2)

# df_can.head())
#   df_can.tail()
# df_can.dtypes
# df_can.info()
# df_can.columns   <-- pandas.core.indexes.base.Index
# df_can.index   <-- pandas.core.indexes.range.RangeIndex
# df_can.columns.values   <-- numpy.ndarray
# df_can.index.values   <-- numpy.ndarray
# df_can.index.tolist()
#   df_can.index.values.tolist()
# df_can.columns.tolist()
#   df_can.columns.values.tolist()
# df_can.shape   <-- returns a tuple

# axis = 0 refers to rows,   axis = 1 refers to columns
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'],
            axis = 1, inplace = True)

df_can.rename(columns = {'OdName':'Country',
                         'AreaName':'Continent',
                         'RegName':'Region'},
              inplace = True)

df_can['Total'] = df_can.sum(axis = 1)

# df_can.isnull().sum()
# df_can.describe()

# Selecting Columns
# df.column_name   <-- returns a pandas series
# df['column']   <-- returns a pandas series
# df[['column1', 'column2', ...]]   <-- returns a pandas dataframe

# df_can.Country
# df_can[['Country', 1980, 1981, 1982]]
# notice that 'Country' is a string whereas years are integers
# we will convert all column names to strings to consistency's sake

# Selecting Rows
# df.loc[label]   <-- index label
# df.iloc[index]   <-- integer reference to index
# df_can[df_can.index == 'Haiti'].T.squeeze()

# df_can.reset()   <-- resets to an integer based index
df_can.set_index('Country', inplace = True)

df_can.index.name = None

# df_can.loc['Japan', 2013]
# df_can.iloc[87, 36]
# df_can.loc['Japan', [1980, 1981, 1982]]   <-- returns a pandas series
# df_can.iloc[87, [3, 4, 5]]

# df_can.columns.map(type)   <-- retrieves the type for the column headers

# convert all columns in df_can to string format
df_can.columns = list(map(str, df_can.columns))

# df_can.columns.map(type)   <-- verify column header type
# df_can.columns   <-- also reveals the column header type

years = list(map(str, range(1980, 2014)))

# create a condition boolean series
# note in the multiple conditional series, each condition is enclosed in ()
condition = df_can['Continent'] == 'Asia'

condition2 = (df_can['Continent'] == 'Asia') & \
             (df_can['Region'] == 'Southern Asia')

# df_can[condition]   <-- boolean based conditional dataframe filtering
#   df_can[condition2]

# print ("Matplotlib version: ", mpl.__version__)
# print (plt.style.available)

# mpl.style.use(['ggplot'])

# generate a pandas series --> haiti
haiti = df_can.loc['Haiti', years]   

haiti.plot()
plt.show()

haiti.index = haiti.index.map(int)

haiti.plot(kind = 'line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.text(2000, 6000, '2010 Earthquake')

# Different types of plots
# bar,  barh,  hist,  box,  kde,  area,  pie,  scatter,  hexbin

plt.show()