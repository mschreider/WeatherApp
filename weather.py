"""
Written by Matthew Schreider
www.github.com/mschreider
"""

import urllib.request, urllib.parse
import json
import time

def get_IP():
    url = "http://checkip.dyndns.org"
    # .decode(utf-8) converts from 'bytes' to 'str'
    data = urllib.request.urlopen(url).read().decode('utf-8')   
    # Parse 76th to 90th index of str
    ip_address = data[76:90]
    return ip_address

def get_weather(ip_address):
    key = "key=d3dc97f5adf0499894b215338200504"
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx?" + key + "&q="+ ip_address + "&format=json&num_of_days=0"
    data = urllib.request.urlopen(url).read()   
    #converts to json file
    json_data = json.loads(data)
    # with open("weather_data.json", 'w') as file:
    #     json.dump(json_data, file)
    current_weather = json_data['data']['current_condition'][0]
    return current_weather  

def print_weather(current_weather):
    print("\tWeather: %s \n"
        "\tTemperature: %s °F \n"
        "\tFeels Like: %s °F\n"
        "\tWind: %s %s mph \n"
        "\tHumidity: %s%% \n"
        "\tPrecipitation: %s in."
        % (current_weather['weatherDesc'][0]['value'],
        current_weather['temp_F'],
        current_weather['FeelsLikeF'],
        current_weather['winddir16Point'],
        current_weather['windspeedMiles'],
        current_weather['humidity'],
        current_weather['precipInches']))

def main():
    print("\n")
    print("Current weather in your area:\n")
    ip_address = get_IP()
    weather = get_weather(ip_address)
    time.sleep(1)
    print_weather(weather)
    print("\n")

if __name__ == "__main__":
    main()