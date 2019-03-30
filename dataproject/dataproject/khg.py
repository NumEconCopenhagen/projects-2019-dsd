import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#countries = ['DK','ZA','US','GB','CN','IN','BR','CA','RU','TR','KR','VN','SE','DE','AL','FR','BG','IT','PK','ID','MX','PL']

countries = ['WLD', 'TSA', 'TMN', 'ECS', 'SSF', 'NAC', 'LCN']

from pandas_datareader import wb
pop = wb.download(indicator='SP.POP.TOTL', country=countries, start=1970, end=2017)
pop.head(3)

gdp = wb.download(indicator='NY.GDP.MKTP.KD', country=countries, start=1970, end=2017)
gdp.head(3)

# Merging data:

merged = pd.merge(gdp,pop, how='inner', on=['country','year'])
merged = merged.reset_index()
merged = merged.rename(columns = {'NY.GDP.MKTP.KD' : 'gdp', 'SP.POP.TOTL' : 'pop'})

merged['gdp_cap'] = merged['gdp'] / merged['pop']

# Sorting data:
merged.sort_values(by=['country','year'], inplace=True)
merged = merged.reset_index(drop = True)
merged.head()

# Indexing:

merged_grouped = merged.groupby('country')
merged_grouped_first = merged_grouped.gdp_cap.first()
merged_grouped_first.name = 'first'

merged.set_index(['country','year'],inplace=True)
merged = merged.join(merged_grouped_first)
merged.reset_index(inplace=True)

merged['indexed'] = merged['gdp_cap']/merged['first']

def plot(fig):
    fig_indexed = fig.set_index('year')
    fig_indexed.groupby(['country'])['indexed'].plot(legend=True);

plot(merged)

# Generating first and last observation:

first = merged.groupby('country')['gdp_cap','pop'].head(1).reset_index()
last = merged.groupby('country')['gdp_cap','pop'].tail(1).reset_index()

print(first)
print(last)

# Generating the growth rate 1970-2017 for GDP per capita and pop:

growth = first/last*100
print(growth)

growth.groupby('index')['pop'].plot(kind='bar',figsize=(10,2))



# Scatter of average one-year growth in GDP per capita and population:

ax = merged.groupby('country').agg(lambda x : x.pct_change(-1).mean()).plot(kind='scatter',x='gdp_cap',y='pop')
ax.set_xlabel('Avg. one-year growth in GDP per capita');
ax.set_ylabel('Avg. one-year growth in population');






# Figure showing the yearly population growth rate in each continent:

fig1 = plt.figure()
fig1 = plt.subplot(111)
merged.set_index('year').groupby('country')['pop'].plot(kind='line',legend=True);
fig1.set_ylabel('GDP');
fig1.invert_xaxis();
box = fig1.get_position()
fig1.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
fig1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5);


fig2 = plt.figure()
fig2 = plt.subplot(111)
merged.set_index('year').groupby('country')['gdp'].plot(kind='line',legend=True);
fig2.set_ylabel('GDP');
fig2.invert_xaxis();
box = fig2.get_position()
fig2.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
fig2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5);



