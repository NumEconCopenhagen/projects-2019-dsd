#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import wb
from numpy import array

#%%
countries = ['WLD', 'TSA', 'TMN', 'ECS', 'TEA', 'SSF', 'NAC', 'LCN']
pop = wb.download(indicator='SP.POP.TOTL', country=countries, start=1970, end=2017)
pop.head(3)

gdp = wb.download(indicator='NY.GDP.MKTP.KD', country=countries, start=1970, end=2017)
gdp.head(3)

# Merging data:

merged = pd.merge(gdp,pop, how='inner', on=['country','year'])
merged = merged.reset_index()
merged = merged.rename(columns = {'NY.GDP.MKTP.KD' : 'gdp', 'SP.POP.TOTL' : 'pop'})

merged['gdp_cap'] = merged['gdp'] / merged['pop']
merged.head()

#%%
# Generating observation:

first= merged.groupby('country')['gdp_cap','pop'].head(1).reset_index(drop=True)
last= merged.groupby('country')['gdp_cap','pop'].head(7).reset_index(drop=True)

print(first, last)

print(last)

#%%
# Generating the growth rate 1970-2017 for GDP per capita and pop:

growth = merged['first'] / merged['last'] * 100
print(growth)


fig1 = plt.figure()
fig1 = plt.subplot()
growth.set_index

#%%
# Scatter of average one-year growth in GDP per capita and population:

ax = merged.groupby('country').agg(lambda x : x.pct_change(-1).mean()).plot(kind='scatter',x='gdp_cap',y='pop')
ax.set_xlabel('Avg. one-year growth in GDP per capita')
ax.set_ylabel('Avg. one-year growth in population')

#%%

fig1 = plt.figure()
fig1 = plt.subplot(111)
merged.set_index('year').groupby('country')['pop'].plot(kind='line',legend=True)
fig1.set_ylabel('GDP')
fig1.invert_xaxis()
box = fig1.get_position()
fig1.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9]) # shrink height by 10% at bottom 
fig1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5) # Put a legend below current axis


fig2 = plt.figure()
fig2 = plt.subplot(111)
merged.set_index('year').groupby('country')['gdp'].plot(kind='line',legend=True)
fig2.set_ylabel('GDP')
fig2.invert_xaxis()
box = fig2.get_position()
fig2.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9]) # shrink height by 10% at bottom 
fig2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5) # Put a legend below current axis


