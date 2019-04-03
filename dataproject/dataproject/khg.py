import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from pandas_datareader import wb

### Downloading data from the World Bank:

continents = ['WLD', 'TSA', 'TMN', 'ECS', 'SSF', 'NAC', 'LCN','TEA']

pop = wb.download(indicator='SP.POP.TOTL', country=continents, start=1970, end=2015)
pop.head(3)

gdp = wb.download(indicator='NY.GDP.MKTP.KD', country=continents, start=1970, end=2015)
gdp.head(3)

### Merging datasets:

merged = pd.merge(gdp,pop, how='inner', on=['country','year'])
merged = merged.reset_index()
merged = merged.rename(columns = {'country' : 'continent', 'NY.GDP.MKTP.KD' : 'gdp', 'SP.POP.TOTL' : 'pop'})

# Generating GDP per capita:

merged['gdp_cap'] = merged['gdp'] / merged['pop']

### Changing type of year-variable from object to float:

merged['year'] = merged.year.astype(float)

### Sorting data:

merged.sort_values(by=['continent','year'], inplace=True)
merged = merged.reset_index(drop = True)

# Indexing GDP per cap and population:

merged_grouped = merged.groupby('continent')
merged_grouped_first = merged_grouped.gdp_cap.first()
merged_grouped_first.name = 'first'

merged.set_index(['continent','year'],inplace=True)
merged = merged.join(merged_grouped_first)
merged.reset_index(inplace=True)

merged['indexed'] = merged['gdp_cap']/merged['first']

### Plot indexed figure:

fig_indexed = plt.figure()
fig_indexed = plt.subplot(111)
merged.set_index('year').groupby('continent')['indexed'].plot(legend=True)
fig_indexed.set_ylabel('GDP per capita, index 1970 = 1')
box = fig_indexed.get_position()
fig_indexed.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
fig_indexed.legend(loc='upper center', bbox_to_anchor = (0.5, -0.15),ncol=5);

# Dropdown widget on pop and gdp_cap development:

def plot(dataframe, continent):
    I = dataframe['continent'] == continent
    fig1, ax = plt.subplots(ncols=2, figsize=(10,4))
    ax_gdp = dataframe.loc[I,:].plot(x = 'year', y = 'gdp_cap', legend = False, ax=ax[0])
    ax_pop = dataframe.loc[I,:].plot(x = 'year', y = 'pop', legend = False, ax=ax[1])
    ax_gdp.set_ylabel('GDP per capita')
    ax_pop.set_ylabel('Population')
    ax_gdp.set_title("GDP per capita 1970-2015 in constant 2010 $US")
    ax_pop.set_title("Population 1970-2015 in 100 millons")
    
widgets.interact(plot, 
    dataframe = widgets.fixed(merged),
    continent = widgets.Dropdown(description='continent', options=merged.continent.unique(), value='Europe & Central Asia')
);

# Creating 5-year growth rates in GDP per cap and in the population in the continents:

merged_5 = merged[merged['year'].isin(['1970','1975','1980','1985','1990','1995','2000','2005','2010','2015'])]
merged_5.set_index(['continent','year'],inplace=True)
merged_5_grouped = merged_5.groupby('continent')
merged_5_change_gdp = merged_5_grouped.gdp_cap.pct_change()
merged_5_change_gdp.name = 'growth_5_gdp'
merged_5_change_pop = merged_5_grouped.pop.pct_change()
merged_5_change_pop.name = 'growth_5_pop'

merged_5 = merged_5.join(merged_5_change_gdp)
merged_5 = merged_5.join(merged_5_change_pop)
merged_5.reset_index(inplace=True)
merged_5 = merged_5[merged_5['year'].isin(['1975','1980','1985','1990','1995','2000','2005','2010','2015'])]

# Bar plot with dropdown widget:

def plot(dataframe, continent):
    I = dataframe['continent'] == continent
    fig1, ax = plt.subplots(ncols=2, figsize=(10,4))
    ax_growth5_gdp = dataframe.loc[I,:].plot.bar(x = 'year', y = 'growth_5_gdp', legend = False, ax=ax[0])
    ax_growth5_pop = dataframe.loc[I,:].plot.bar(x = 'year', y = 'growth_5_pop', legend = False, ax=ax[1])
    ax_growth5_gdp.set_ylabel('Growth in pct.')
    ax_growth5_gdp.set_xlabel('5-year period')
    ax_growth5_pop.set_ylabel('Growth in pct.')
    ax_growth5_pop.set_xlabel('5-year period')

widgets.interact(plot, 
    dataframe = widgets.fixed(merged_5),
    continent = widgets.Dropdown(description='continent', options=merged_5.continent.unique(), value='Europe & Central Asia')
);


# Yearly growth rate in GDP and population:

merged_yearly = merged.groupby('continent')['gdp_cap'].pct_change()
merged_yearly.head(50)


# Generating first and last observation and growth rate over the 
# whole period:

first = merged.groupby('continent')['gdp_cap','pop'].head(1).reset_index()
last = merged.groupby('continent')['gdp_cap','pop'].tail(1).reset_index()

print(first)
print(last)

growth = first/last*100
print(growth)

growth.groupby('index')['pop'].plot(kind='bar',figsize=(10,2))


# Scatter of average one-year growth in GDP per capita and population:

ax = merged.groupby('continent').agg(lambda x : x.pct_change(-1).mean()).plot(kind='scatter',x='gdp_cap',y='pop')
ax.set_xlabel('Avg. one-year growth in GDP per capita');
ax.set_ylabel('Avg. one-year growth in population');



# Figure showing the yearly population growth rate in each continent:

fig1 = plt.figure()
fig1 = plt.subplot(111)
merged.set_index('year').groupby('continent')['pop'].plot(kind='line',legend=True);
fig1.set_ylabel('Pop');
box = fig1.get_position()
fig1.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
fig1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5);


fig2 = plt.figure()
fig2 = plt.subplot(111)
merged.set_index('year').groupby('continent')['gdp'].plot(kind='line',legend=True);
fig2.set_ylabel('GDP');
box = fig2.get_position()
fig2.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
fig2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5);



