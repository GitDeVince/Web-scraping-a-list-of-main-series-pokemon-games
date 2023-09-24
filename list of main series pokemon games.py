import pandas as pd
from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon_video_games"

tables = pd.read_html(url)
df = tables[1]
df.to_csv('main series pokemon games.csv')
