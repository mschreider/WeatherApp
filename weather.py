import urllib.request, urllib.parse
import json
import time, sys

def get_IP():
    url = "http://checkip.dyndns.org"
    data = urllib.request.urlopen(url).read().decode('utf-8')   # .decode(utf-8) converts from 'bytes' to 'str'
    # print(type(data))
    ip_address = data[76:90]    # Parse 76th to 90th index of str
    return ip_address

def get_information(ip_address):
    key = "key=d3dc97f5adf0499894b215338200504"
    url = "http://api.worldweatheronline.com/premium/v1/weather.ashx?" + key + "&q="+ ip_address + "&format=json&num_of_days=0&includelocation=yes"
    data = urllib.request.urlopen(url).read()   
    json_data = json.loads(data)    #converts to json file
    # with open("weather_data.json", 'x') as file:
    #     json.dump(json_data, file)
    current_weather = json_data['data']['current_condition'][0]
    current_location = json_data['data']['nearest_area'][0]
    return current_weather, current_location

def print_location(current_location):
    print("%s, %s, %s\n" % (current_location['areaName'][0]['value'], current_location['region'][0]['value'], current_location['country'][0]['value']))
    
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
    end_time = time.time() + 4
    while time.time() < end_time:    # performs while loop for 5 seconds
        for x in range(0,5):
            print("Getting weather information for your area%s" % ("."*x), end="\r")
            time.sleep(0.3)
            sys.stdout.write('\033[K\033[G')
            if x == 4:
                x=0
    print("Current weather in your area:\n")
    ip_address = get_IP()
    weather, location = get_information(ip_address)
    print_location(location)
    time.sleep(0.5)
    print_weather(weather)
    print("\n")

if __name__ == "__main__":
    main()