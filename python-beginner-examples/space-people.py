#web request for the website that stores space data via api. 

# need to install requests library command: python3 -m pip install requests

import requests

# send HTTP and JSON data is returned via HTTP response.
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('The people currently in space are:')
#the api has a parameter people
for p in json['people']:
    print(p['name'])


# Make a virtual environment
# python3 -m venv virtualenv
# source virtualenv/bin/activate
# python3 -m pip install requests