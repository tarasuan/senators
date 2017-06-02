import requests

# make API call to Sunlight Foundation
r = requests.get('https://congress.api.sunlightfoundation.com/votes?roll_id=h256-2017&per_page=all&fields=voter_ids')
#print r.text
#print r.headers

votes_response = r.json()
votes = votes_response['results'][0]['voter_ids']

#print votes['G000582']

# get congresspersons info for the voter_ids in yays
r2 = requests.get('https://congress.api.sunlightfoundation.com/legislators?chamber=house&per_page=all&fields=bioguide_id,first_name,last_name,gender,party,district,middle_name,nick_name,state,state_name')

#print r2.text

j2 = r2.json()

#print j2['results'][0]
congress = j2['results']

# add votes to congress
for person in congress:
  #make variable for bioguide
  bioguide_id = person['bioguide_id']
  if bioguide_id in votes:
    # add the vote to the record
    person['ahca'] = votes[bioguide_id]
    # why did votes[bioguide_id] give keyerror on missing data?

# make a new dict
congresspersons = {}

# loop through list
for item in congress:
  # make district object
  district = str(item['state']) + "-" + str(item['district'])
  congresspersons[district] = item

import pandas as pd

#df = pd.concat(map(pd.DataFrame, congresspersons.itervalues()), keys=congresspersons.keys()).stack().unstack(0)
#df = pd.Panel.from_dict(congresspersons).to_frame(index=1)
df = pd.DataFrame.from_dict(congresspersons, orient='index')

df.to_csv('votes_df.csv', encoding='utf-8')
