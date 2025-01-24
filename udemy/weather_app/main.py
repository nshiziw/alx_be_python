from typing import Union 
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests

app = FastAPI()

def get_temp(forecast_url):
    r = requests.get(forecast_url).json()
    day_temp = r['properties']['periods'][0]
    return {
        "temperature": day_temp["temperature"],
        "wind_speed": day_temp["windSpeed"],
        "icon": day_temp["icon"],
        "forecast": day_temp["shortForecast"],
    }

def getLoc(ip):
    r = requests.get('https://ipinfo.io/{ip}/json'.format(ip=ip)).json()
    return {
        "city": r["city"],
        "loc": r["loc"]
    }

def getGrid(loc):
    r = requests.get('https://api.weather.gov/points/{loc}'.format(loc=loc)).json()
    return r['properties']['forecast']

@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    client_host = request.client.host
    client_host = '63.116.61.253' #TODO, will remove it
    location = getLoc(client_host)
    forecast_url = getGrid(location["loc"])
    temp = get_temp(forecast_url)
    temperature = temp["temperature"]
    icon = temp["icon"]
    wind_speed = temp["wind_speed"]
    pre_pos = 67
    city = location["city"]
    time = "15:07"
    forecast = temp["forecast"]
    html_content = """
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Weather App</title>
                <!-- Tailwind CSS CDN -->
                <script src="https://cdn.tailwindcss.com"></script>
            </head>
            <body class="bg-gray-100">
                <div class="flex justify-center items-center py-10">
                <div class="bg-white p-6 rounded-3xl shadow-xl max-w-sm w-full">
                    <div class="flex justify-between items-center">
                    <h6 class="text-xl font-semibold">{city}</h6>
                    <h6 class="text-sm text-gray-600">{time}</h6>
                    </div>

                    <div class="flex flex-col items-center my-8">
                    <h6 class="text-6xl font-bold">{temperature}°F</h6>
                    <span class="text-sm text-gray-500">{forecast}</span>
                    </div>

                    <div class="flex items-center justify-between">
                    <div class="flex flex-col text-sm text-gray-600">
                        <div class="flex items-center mb-2">
                        <i class="fas fa-wind text-gray-600"></i>
                        <span class="ml-2">{wind_speed}</span>
                        </div>
                        <div class="flex items-center mb-2">
                        <i class="fas fa-tint text-gray-600"></i>
                        <span class="ml-2">{pre_pos}%</span>
                        </div>
                        <div class="flex items-center">
                        <i class="fas fa-sun text-gray-600"></i>
                        <span class="ml-2">0.2h</span>
                        </div>
                    </div>
                    <div class="w-24">
                        <img
                        src="{icon}"
                        alt="Weather Icon"
                        class="w-full rounded-full"
                        />
                    </div>
                    </div>
                </div>
                </div>

                <!-- Font Awesome CDN -->
                <script src="https://kit.fontawesome.com/a076d05399.js"></script>
            </body>
        </html>

    """.format(temperature = temperature,time = time, icon = icon,forecast = forecast, wind_speed = wind_speed, city = city, pre_pos = pre_pos)

    return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id,"q": q}