from bs4 import BeautifulSoup
import urllib

r = urllib.urlopen('https://en.wikipedia.org/wiki/List_of_current_United_States_Senators').read()
soup = BeautifulSoup(r, 'html.parser')

tables = soup.find_all('table')
senator_table = tables[6]

rows = senator_table.find_all('tr')

senators = {}

# loop through tr's

for row in rows:
  cols = row.find_all('td')

  for index, col in enumerate(cols):
    if index == 4:
      # still need to clean up the name field
      # this doesn't work -- print soup.find('title').find(text=True, recursive=False)
      # ignore span class="sortkey" ?
      senator_name = col.a.get_text()
      senators[senator_name] = {}
      senators[senator_name]['state'] = cols[1].get_text()
      senators[senator_name]['party'] = cols[5].get_text()

print senators
