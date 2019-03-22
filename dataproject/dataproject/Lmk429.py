#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import wb
from numpy import array

#%%
countries = ['DK','ZA','TR','AL','US','GB','CN','IN','BR','CA','RU','KR','VN','SE','DE','FR','BG','IT','PK','ID','MX','PL']

pop = wb.download(indicator='SP.POP.TOTL',    country=countries, start=1970, end=2017)
gdp = wb.download(indicator='NY.GDP.PCAP.KD', country=countries, start=1970, end=2017)

#pop = pop.rename(columns = {'SP.POP.TOTL':'population'})
#pop = pop.reset_index()
#gdp = gdp.rename(columns = {'NY.GDP.PCAP.KD' :'GDP'})
#gdp = gdp.reset_index()

GDPpop = pd.merge(gdp, pop,how='inner',on=['country', 'year'])
GDPpop = GDPpop.rename(columns = {'NY.GDP.PCAP.KD' :'gdp', 'SP.POP.TOTL':'population'})
GDPpop = GDPpop.reset_index()

#%%
figur1 = plt.figure()
figur1 = plt.subplot(111)
GDPpop.set_index('year').groupby('country')['gdp'].plot(kind='line', legend=True);
figur1.set_ylabel('gdp');
box = figur1.get_position() # find plot coordinates 
figur1.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9]) # shrink height by 10% at bottom 
figur1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5); # Put a legend below current axis
  

