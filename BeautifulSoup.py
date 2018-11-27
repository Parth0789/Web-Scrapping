import requests
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd

place = []
username = []
xp =[]
np.set_printoptions(sign = ' ')
#get the data
data = requests.get('https://umggaming.com/leaderboards')

#load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

leaderboad = soup.find('table', {'id': 'leaderboard-table'})
tbody = leaderboad.find('tbody')

for tr in tbody.find_all('tr'):
    place.append(tr.find_all('td')[0].text.strip())
    username.append(tr.find_all('td')[1].find_all('a')[1].text.strip())
    xp.append(tr.find_all('td')[3].text.strip())

df = pd.DataFrame({'Place':place, 'Username':username, 'XP':xp})
df.to_csv('output.csv')

