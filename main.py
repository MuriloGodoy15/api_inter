from fastapi import FastAPI
import requests as request
import random

app = FastAPI()

goodwe_api_url = "https://apigoodwe.onrender.com"

def get_consumo():
    return {"consumo": round(random.uniform(1.2, 3.8), 2)}

@app.get("/")
def root():
    return {"message": "API Intermediária está no ar"}

@app.post("/alexa")
async def handle_alexa(request: Request):
    body = await request.json()
    intent_name = body['request']['intent']['name']

    if intent_name == "ConsumoAtualIntent":
        consumo = get_consumo()
        return {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": f"Seu consumo atual é de {consumo['consumo']} kilowatts"
                },
                "shouldEndSession": True
            }
        }

    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Desculpe, não entendi esse comando"
            },
            "shouldEndSession": True
        }
    }
