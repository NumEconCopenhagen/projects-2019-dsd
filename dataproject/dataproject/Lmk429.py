
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from pandas_datareader import wb
pop_wb = wb.download(indicator='SP.POP.TOTL', country=['SE','DK','NO'], start=1960, end=2017)
pop_wb = pop_wb.rename(columns = {'SP.POP.TOTL':'population'})
pop_wb = pop_wb.reset_index()
pop_wb.head(30)
