import requests

start_url = 'https://www.iseecars.com/used-cars/used-tesla-for-sale'

downloaded_page = requests.get(start_url)

print(downloaded_page.text)