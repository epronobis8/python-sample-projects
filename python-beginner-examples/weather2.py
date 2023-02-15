import requests

api_key = ""
city = "Baltimore"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()
print(json)

# reference weather.json for an example of the data for this.
description = json.get("weather")[0].get("description")
print("Today's forecast is", description)

min_temp = json.get("main").get("temp_min")
print("Todays low is", min_temp)

max_temp = json.get("main").get("temp_max")
print("Todays max is", max_temp)
