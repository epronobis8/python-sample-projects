import json
import requests
import logging
import boto3

client = boto3.client('ssm')

def get_weather_desc_and_temp():
    parm = client.get_parameter(Name='weather-api-key', WithDecryption=True)
    api_key = parm['Parameter']['Value']
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

def lambda_handler(event, context):
    weather_dict = get_weather_desc_and_temp()
    print("Todays forecast is", weather_dict.get('description'))
    print("Todays low is", weather_dict.get('min_temp'))
    print("Todays high is", weather_dict.get('max_temp'))