
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Download and prase hte HTML
start_url = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'

# Download the HTML from start_url
downloaded_html = requests.get(start_url)

# Prase the HTML with Beautiful soup and create a soup object
soup = BeautifulSoup(downloaded_html.text)

# Save a local copy
with open('downloaded.html', 'w') as file:
    file.write(soup.prettify())