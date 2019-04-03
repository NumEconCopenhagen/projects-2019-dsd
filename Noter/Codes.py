#%%
#GDP constant 2010 USdollar

countries = ['DK','ZA','TR','AL','US','GB','CN','IN','BR','CA','RU','KR','VN','SE','DE','FR','BG','IT','PK','ID','MX','PL']
variables = ['SP.POP.TOTL', 'NY.GDP.MKTP.KD','NY.GDP.PCAP.KD']
df_names = {
    'SP.POP.TOTL':'population',
    'NY.GDP.MKTP.KD' : 'GDP',
    'NY.GDP.PCAP.KD' :'GDPcap'

}

df =  wb.download(indicator=variables, country=countries, start=1980, end=2017).reset_index()
df = df.rename(columns=df_names)

df.head()

#%%
figur1 = plt.figure()
figur1 = plt.subplot(111)
df.set_index('year').groupby('country')['GDPcap'].plot(kind='line', legend=True)
figur1.set_ylabel('GDPcap')
box = figur1.get_position() # find plot coordinates 
figur1.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9]) # shrink height by 10% at bottom 
figur1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),ncol=5) # Put a legend below current axis


#Måden hvorpå man omdanner til numeric
merged['year'] = merged['year'].apply(pd.to_numeric)

#Eksempel
merged['year'] = merged['year'].apply(pd.to_numeric)
is_div5 = numerged%5==0
print(is_div5.head(33))

merged_div5 = merged[is_div5]
print(merged_div5.shape)
merged_div5.head(5)

# Growth in the period 1970-2017 for each continent:

merged_grouped_last = merged_grouped.gdp_cap.last()
merged_grouped_last.name = 'last'

merged.set_index(['continent','year'],inplace=True)
merged = merged.join(merged_grouped_last)
merged.reset_index(inplace=True)

merged['g_total'] = merged['last']/merged['first']*100