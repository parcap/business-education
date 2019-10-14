import pandas as pd

animals_list = ['Tiger', 'Bear', 'Moose']     # animals is a list
animals_series = pd.Series(animals)           # notice the indexing of the list

sports_dict = {'Archery': 'Bhutan',
               'Golf': 'Scotland',
               'Sumo': 'Japan',
               'Taekwondo': 'South Korea'}

sports_series = pd.Series(sports_dict)

sports_series.index         # returns the index of the series

animals2_series = pd.Series(['Tiger', 'Bear', 'Moose'],
                            index = ['India', 'America', 'Canada'])

# Note how Series creation depends on index setting and dictionary structure
sports2_series = pd.Series(sports, index = ['Archery', 'Golf', 'Hockey'])
sports3_series = pd.Series(sports, index = ['Bhutan', 'Scotland', 'India'])

sports3_series.iloc[2:3]
