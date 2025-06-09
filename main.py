from fastapi import FastAPI
import requests as request

app = FastAPI()

goodwe_api_url = "http://localhost:8001/"

@app.get("/status")
def get_status():
    try:
        r = request.get(f"{goodwe_api_url}/status")
        return r.json()
    except: 
        return {"error": "Failed to fetch status from GoodWe API"}
   
@app.get("/consumo")
def get_consumo():
    try:
        r = request.get(f"{goodwe_api_url}/consumo")
        return r.json()
    except: 
        return {"error": "Failed to fetch consumo from GoodWe API"}

@app.get("/geracao")
def get_geracao():
    try:
        r = request.get(f"{goodwe_api_url}/geracao")
        return r.json()
    except: 
        return {"error": "Failed to fetch geracao from GoodWe API"}
