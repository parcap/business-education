'''
Area Plots


'''
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

df_can = pd.read_excel(
            'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-' \
            'data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
            sheetname = 'Canada by Citizenship',
            skiprows = range(20),
            skip_footer = 2)

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'],
            axis = 1, inplace = True)

df_can.rename(columns = {'OdName':'Country',
                         'AreaName':'Continent',
                         'RegName':'Region'},
              inplace = True)

df_can['Total'] = df_can.sum(axis = 1)

df_can.set_index('Country', inplace = True)

df_can.index.name = None

df_can.columns = list(map(str, df_can.columns))

years = list(map(str, range(1980, 2014)))

df_can.sort_values(['Total'], ascending = False, axis = 0, inplace = True)

df_top5 = df_can.head(5)
df_top5 = df_top5[years].transpose()

df_top5.plot(kind = 'area')
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()