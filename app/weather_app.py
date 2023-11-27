from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
import uvicorn
import json
import requests

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

url = 'http://fa689197-ad3e-42d9-b11a-aa6dc6cd6b5a.francecentral.azurecontainer.io/score'
headers = {'Content-Type':'application/json'}

class weather(BaseModel):
    Temperature_C: int
    Humidity: int
    Wind_speed_kmph: int
    Wind_bearing_degrees: int
    Visibility_km: int
    Pressure_millibars: int
    Current_weather_condition: int

@app.get("/")
def home(request: Request):
	return templates.TemplateResponse("index.html", {"request": request})


@app.post('/predict', response_class=HTMLResponse)
async def make_predictions(request: Request, Temperature_C: int = Form(...), Humidity: int = Form(...), Wind_speed_kmph: int = Form(...), Wind_bearing_degrees: int = Form(...), Visibility_km: int = Form(...), Pressure_millibars: int = Form(...), Current_weather_condition: int = Form(...)):
    
    inference_data = {
        "Inputs": {
            "data": [
                {
                    "Temperature_C": int(Temperature_C),
                    "Humidity": int(Humidity),
                    "Wind_speed_kmph": int(Wind_speed_kmph),
                    "Wind_bearing_degrees": int(Wind_bearing_degrees),
                    "Visibility_km": int(Visibility_km),
                    "Pressure_millibars": int(Pressure_millibars),
                    "Current_weather_condition": int(Current_weather_condition)
                }
            ]
        },
        "GlobalParameters": {
            "method": "predict"
        }
    }

    inference_data = json.dumps(inference_data) 
    r = requests.post(url, data=inference_data, headers=headers)
    result = r.content

    response_content_str = r.content.decode('utf-8')
    response_json = json.loads(response_content_str)
    result_value = response_json["Results"][0]

    if (result_value == 1):
        result = "No rain"
    else:
        result = "Rain"
   
    return templates.TemplateResponse("index.html", {"request": request, "result":result})



