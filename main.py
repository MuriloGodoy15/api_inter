from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

mock_data = {
    "status": "Operando normalmente",
    "consumo": "3.0 kW",
    "geracao": "4.0 kW"
}

@app.get("/status")
def get_status():
    return {"status": mock_data["status"]}

@app.get("/consumo")
def get_consumo():
    return {"consumo": mock_data["consumo"]}

@app.get("/geracao")
def get_geracao():
    return {"geracao": mock_data["geracao"]}
