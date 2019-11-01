import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

mpl.style.use("ggplot")
print('Matplotlib version: ', mpl.__version__)
set_figsize = (12, 8)


def show_plot(df, plot_kind, plot_title, y_label="", x_label="",
              show_legend_title=False, figsize=(10, 6)):
    if plot_kind == "hist":
        df.plot(kind=plot_kind, xticks=bin_edges, figsize=figsize)
    else:
        df.plot(kind=plot_kind, figsize=figsize)
    plt.title(plot_title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    if not show_legend_title:
        plt.legend(title=None)

    plt.show()

web_address = "https://s3-api.us-geo.objectstorage.softlayer.net/" \
              "cf-courses-data/CognitiveClass/DV0101EN/labs/" \
              "Data_Files/Canada.xlsx"

top_countries = 5
year_of_interest = "2013"
country_of_interest = "Iceland"

df_canada = pd.read_excel(web_address,
                          sheetname="Canada by Citizenship",
                          skiprows=range(20),
                          skip_footer=2)

# Data munging on Canada immigration dataframe
df_canada.columns = list(map(str, df_canada.columns))

drop_columns = ["Type", "Coverage", "AREA", "REG", "DEV"]
df_canada.drop(drop_columns, axis=1, inplace=True)

rename_columns = ({"OdName": "Country", "AreaName": "Continent",
                   "RegName": "Region"})
df_canada.rename(columns=rename_columns, inplace=True)

df_canada.set_index("Country", inplace=True)
df_canada["Total"] = df_canada.sum(axis=1)
df_canada.sort_values(["Total"], ascending=False, axis=0, inplace=True)

# Generate top countries area plot
df_canada_top = df_canada.head(top_countries)
years = list(map(str, range(1980, 2014)))
df_canada_top = df_canada_top[years].transpose()
show_plot(df_canada_top, plot_kind="area", figsize=set_figsize,
          plot_title="Top Immigration Trend by Countries",
          y_label="Number of Immigrants", x_label="Years")

# Generate immigration by country histogram
df_canada_year = df_canada[year_of_interest]
count, bin_edges = np.histogram(df_canada_year)
show_plot(df_canada_year, plot_kind="hist",  figsize=set_figsize,
          plot_title="Top Immigration Trend by Countries",
          y_label="Number of Countries",
          x_label="Number of Immigrants")

# Generate immigration by yeaer for a given country as a bar chart
df_canada_country = df_canada.loc[country_of_interest, years]
show_plot(df_canada_country, plot_kind="barh", figsize=set_figsize,
          plot_title="Immigration to Canada by Year",
          y_label="Number of Immigrants",
          x_label="Year")

# Generate a pie chart show share of immigration by continent
df_canada_continents = df_canada.groupby("Continent", axis=0).sum()
show_plot(df_canada_continents["Total"], plot_kind='pie', figsize=(10, 10),
          plot_title="Immigration to Canada by Continent [1980-2013]")
