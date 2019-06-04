web_list = []
web_list.append('https://www.imdb.com/search/title?release_date=2018-01-01,2019-01-01&sort=num_votes,desc&ref_=adv_prv')
for i in range(51,1000,50):
  tmp = 'https://www.imdb.com/search/title?release_date=2018-01-01,2019-01-01&sort=num_votes,desc&start=' + str(i) + '&ref_=adv_nxt'
  web_list.append(tmp)
print(web_list)
from requests import get
from bs4 import BeautifulSoup
# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

for item in web_list:
  url = item
  
  response = get(url)
  html_soup = BeautifulSoup(response.text, 'html.parser')
  #print(response.text[:500])
  movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
  print(type(movie_containers))
  print(len(movie_containers))
  print(len(names))

  # Extract data from individual movie container
  for container in movie_containers:
    # If the movie has Metascore, then extract:
    if container.find('div', class_ = 'ratings-metascore') is not None:
      # The name
      name = container.h3.a.text
      names.append(name)
      # The year
      year = container.h3.find('span', class_ = 'lister-item-year').text
      years.append(year)
      # The IMDB rating
      imdb = float(container.strong.text)
      imdb_ratings.append(imdb)
      # The Metascore
      m_score = container.find('span', class_ = 'metascore').text
      metascores.append(int(m_score))
      # The number of votes
      vote = container.find('span', attrs = {'name':'nv'})['data-value']
      votes.append(int(vote))

import pandas as pd
test_df = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes
})
print(test_df.info())
test_df
test_df.to_csv('Moviedata.csv', header=True, index=False, encoding='utf-8')