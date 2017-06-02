from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


df = pd.read_csv('MOC.csv', sep=',', usecols = (
    'first_name',
    'last_name',
    'state',
    'district',
    'gender',
    'population',
    'num_uninsured',
    'num_deaths',
    'medicaid_expansion_state',
    'swing_left_district',
    'freedom_caucus_member',
    'percent_vote_2016',
    'percent_vote_clinton',
    'percent_vote_trump',
    'president_vote_margin')
)

df.describe()

# define cols to clean and convert to numeric
cols_to_convert = ['population', 'num_uninsured']

# ALTERNATE ONE
# import re
# df['population'] = df['population'].astype(str).map(lambda x: re.sub(r"[^0-9]+", "", x))

# BUSTED
# def strip_comma(value):
#   value = value.replace(',','')

strip_comma = lambda x: x.replace(',','')

df[cols_to_convert] = df[cols_to_convert].astype(str).applymap(strip_comma)

numericize = lambda x: pd.to_numeric(x, errors='coerce')

df[cols_to_convert] = df[cols_to_convert].applymap(numericize)

# GENDER 
df.pivot_table(index='gender', aggfunc='mean')
pd.crosstab(df.gender, df.medicaid_expansion_state)
pd.crosstab((df.gender, df.swing_left_district), (df.medicaid_expansion_state, df.freedom_caucus_member))

# POPULATION HISTOGRAM
plt.hist(df['population'].dropna())
df['population'].hist(color='DarkBlue')

# TRUMP MARGIN WIN
plt.hist(df['percent_vote_trump'].dropna())

# SCATTERS OF NUMERICAL COLS and RELATIONSHIPS
df.plot.scatter(x='num_uninsured', y='percent_vote_trump', color='DarkGreen')
df.plot.scatter(x='population', y='percent_vote_trump', color='DarkGreen')
# saved: 'uninsured_trump.png' df.plot.scatter(x='num_uninsured', y='percent_vote_trump', color='DarkGreen')
# saved: 'deaths_trump.png' df.plot.scatter(x='num_deaths', y='percent_vote_trump', color='DarkGreen')
df.plot.scatter(x='population', y='percent_vote_trump', color='DarkGreen')
plt.savefig('population_trump')

# Lets look at the correlation of the two groups of features
# population, uninsured and deaths are correlated
# all the stats about pres election are correlated
print df.corr()

# Conclusion - there is not much interesting in the data in terms of "gotchas!"

df['uninsured_population'] = df['num_uninsured'] / df['population'][0]
df['uninsured_population'].hist(color='DarkBlue')
plt.show()

df.plot.scatter(x='uninsured_population', y='percent_vote_trump', color='DarkGreen')
plt.savefig('uninsured_population_trump')

# if it were a map, it would have to be a district map

