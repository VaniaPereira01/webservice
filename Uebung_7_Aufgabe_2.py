# Aufgabe 2:
# Erstellen Sie einen Webservice um Koordinaten von LV95 nach WGS84 zu
# transformieren und umgekehrt.
# Der Webdiesnst kann zum Beispiel so aussehen:
# http://localhost:8000/wgs84lv95?lng=0.0000&lat=0.0000
# # Die Rückgabe ist ein JSON mit sinnvollen Parameternamen.


import uvicorn
from fastapi import FastAPI
from fastapi import responses
from fastapi.staticfiles import StaticFiles
import pyproj
from pyproj import Transformer

app = FastAPI()
lv95 = "EPSG:2056"
wgs84 = "EPSG:4326"

t1 = Transformer.from_crs(wgs84,lv95)
t2 = Transformer.from_crs(lv95,wgs84)
@app.get("/wgs84lv95")
async def wgs84lv95(lat: float=0, lng:float=0):
    resultat =t1.transform(lat,lng)
    return {"LV95-Koordinaten" :resultat}

@app.get("/lv95wgs84")
async def lv95wgs84(lat: float=0, lng:float=0):
    resultat =t2.transform(lat,lng)
    return {"WGS84-Koordinaten" :resultat}

uvicorn.run(app, host="localhost", port=8000)

# http://localhost:8000/wgs84lv95?lat=46.8182&lng=8.2275
# http://localhost:8000/lv95wgs84?lat=600000&lng=200000