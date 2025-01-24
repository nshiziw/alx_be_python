from typing import Union 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <div class="row d-flex justify-content-center py-5">
                <div class="col-md-8 col-lg-6 col-xl-5">

                    <div class="card text-body" style=" border-radius: 35px;">
                    <div class="card-body p-4">

                        <div class="d-flex">
                        <h6 class="flex-grow-1">Warsaw</h6>
                        <h6>15:07</h6>
                        </div>

                        <div class="d-flex flex-column text-center mt-5 mb-4">
                        <h6 class="display-4 mb-0 font-weight-bold"> 13°C </h6>
                        <span class="small" style="color: #868B94">Stormy</span>
                        </div>

                        <div class="d-flex align-items-center">
                        <div class="flex-grow-1" style="font-size: 1rem;">
                            <div><i class="fas fa-wind fa-fw" style="color: #868B94;"></i> <span class="ms-1"> 40 km/h
                            </span>
                            </div>
                            <div><i class="fas fa-tint fa-fw" style="color: #868B94;"></i> <span class="ms-1"> 84%
                            </span></div>
                            <div><i class="fas fa-sun fa-fw" style="color: #868B94;"></i> <span class="ms-1"> 0.2h
                            </span></div>
                        </div>
                        <div>
                            <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu1.webp"
                            width="100px">
                        </div>
                        </div>

                    </div>
                    </div>

                </div>
            </div>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id,"q": q}