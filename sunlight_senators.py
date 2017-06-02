import requests

# get senator info for the voter_ids in yays
r2 = requests.get('https://congress.api.sunlightfoundation.com/legislators?chamber=house&fields=bioguide_id,first_name,last_name,gender,party,district,middle_name,nick_name,state,state_name')

#print r2.text

j2 = r2.json()

assembly = j2['results']

print assembly

#make a new dict
#assembly_yays = {}

# loop through assembly

# if 
