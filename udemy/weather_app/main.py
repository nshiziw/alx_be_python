from typing import Union 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_items():
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
                    <h6 class="text-xl font-semibold">Warsaw</h6>
                    <h6 class="text-sm text-gray-600">15:07</h6>
                    </div>

                    <div class="flex flex-col items-center my-8">
                    <h6 class="text-6xl font-bold">13°C</h6>
                    <span class="text-sm text-gray-500">Stormy</span>
                    </div>

                    <div class="flex items-center justify-between">
                    <div class="flex flex-col text-sm text-gray-600">
                        <div class="flex items-center mb-2">
                        <i class="fas fa-wind text-gray-600"></i>
                        <span class="ml-2">40 km/h</span>
                        </div>
                        <div class="flex items-center mb-2">
                        <i class="fas fa-tint text-gray-600"></i>
                        <span class="ml-2">84%</span>
                        </div>
                        <div class="flex items-center">
                        <i class="fas fa-sun text-gray-600"></i>
                        <span class="ml-2">0.2h</span>
                        </div>
                    </div>
                    <div class="w-24">
                        <img
                        src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu1.webp"
                        alt="Weather Icon"
                        class="w-full"
                        />
                    </div>
                    </div>
                </div>
                </div>

                <!-- Font Awesome CDN -->
                <script src="https://kit.fontawesome.com/a076d05399.js"></script>
            </body>
        </html>

    """

    return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id,"q": q}