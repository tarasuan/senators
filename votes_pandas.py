import pandas as pd

df = pd.read_csv('votes_df.csv')

#count nays
print len(df[df.ahca == 'Yea'])