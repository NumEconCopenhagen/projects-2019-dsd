#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import wb
from numpy import array

#%%
#GDP constant 2010 USdollar

countries = ['DK','ZA','TR','AL','US','GB','CN','IN','BR','CA','RU','KR','VN','SE','DE','FR','BG','IT','PK','ID','MX','PL']

variables = ['SP.POP.TOTL', 'NY.GDP.MKTP.KD','NY.GDP.PCAP.KD']

df_names = {
    'SP.POP.TOTL':'population',
    'NY.GDP.MKTP.KD' : 'GDP',
    'NY.GDP.PCAP.KD' :'GDPcap'

}

df =  wb.download(indicator=variables, country=countries, start=1970, end=2017).reset_index()
df = df.rename(columns=df_names)
df.head()

#df[""] = df[""] / df[""]


#%%
figur1 = plt.figure()
figur1 = plt.subplot(111)
df.set_index('year').groupby('country')[["year", 'GDPcap']].plot(x= "year", y="GDPcap", kind='line', legend=True)
figur1.set_ylabel('GDPcap')
figur1.set_ylabel('GDPcap')
box = figur1.get_position() # find plot coordinates 
figur1.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9]) # shrink height by 10% at bottom 
figur1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5) # Put a legend below current axis
  

