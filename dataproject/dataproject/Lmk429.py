
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

#%%
from pandas_datareader import wb
countries = ['DK','ZA','US','GB','CN','IN','BR','CA','RU','KR','VN','SE','DE','FR','BG','IT','PK','ID','MX','PL']
pop_wb = wb.download(indicator='SP.POP.TOTL', country=countries, start=1960, end=2017)
pop_wb = pop_wb.rename(columns = {'SP.POP.TOTL':'population'})
pop_wb = pop_wb.reset_index()
pop_wb.head(174)
pop = wb.download(indicator='SP.POP.TOTL',    country=countries, start=1970, end=2017)
gdp = wb.download(indicator='NY.GDP.PCAP.KD', country=countries, start=1970, end=2017)
