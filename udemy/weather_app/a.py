import requests
def getTemp():
    r = requests.get('https://api.weather.gov/gridpoints/TOP/31,80/forecast').json()
    day_temp = r['properties']['periods'][0]
    return {
        "temperature": day_temp["temperature"],
        "wind_speed": day_temp["windSpeed"],
        "icon": day_temp["icon"],
        "forecast": day_temp["shortForecast"],
    }
print(getTemp())