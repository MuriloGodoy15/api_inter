from fastapi import FastAPI
import requests as request
from apigoodwe import goodwe

app = FastAPI()



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
    
@app.get("/")
def root():
    return {"message": "está no ar"}

@app.post("/alexa")
async def handle_alexa(request: request):
    body = await request.json()
    intent_name = body['request']['intent']['name']

    if intent_name == 'GetConsumoIntent':
        consumo = get_consumo()
        return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": f"Seu consumo atual é de {consumo['consumo']} KW/h"
                },
                "shouldEndSession": True
            }
        }
    
    return{
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": f"Não entendi o comando"
                },
                "shouldEndSession": True
            }
        }
    return 
    JSONResponse(content=response)