import requests

def get_weather_desc_and_temp():
    api_key = "13b6b0266bedf867e02e8c065dcc1c9d"
    city = "Baltimore"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()

    # reference weather.json for an example of the data for this.
    description = json.get("weather")[0].get("description")
    min_temp = json.get("main").get("temp_min")
    max_temp = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': min_temp,
            'temp_max': max_temp}

def main():
    weather_dict = get_weather_desc_and_temp()
    print("Todays forecast is", weather_dict.get('description'))
    print("Todays low is", weather_dict.get('min_temp'))
    print("Todays high is", weather_dict.get('max_temp'))

main()