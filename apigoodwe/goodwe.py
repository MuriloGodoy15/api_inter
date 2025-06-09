from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/status")
def get_status():
    opcoes_de_status = ["Operando normalmente", "Modo economia", "Falha de comunicação", "Bateria baixa"]
    return {"status": random.choice(opcoes_de_status)}

@app.get("/consumo")
def get_consumo():
    consumo = round(random.uniform(0.5, 5.0), 2)  # kW
    return {"consumo": f"{consumo} kW"}

@app.get("/geracao")
def get_geracao():
    geracao = round(random.uniform(1.0, 7.5), 2)  # kW
    return {"geracao": f"{geracao} kW"}
