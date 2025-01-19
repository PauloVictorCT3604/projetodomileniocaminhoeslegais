from fastapi import APIRouter, HTTPException
from models.motorista import Motorista
from services.motorista_service import criar_motorista

roteador = APIRouter()

@roteador.post("/motoristas", response_model=Motorista)
def criar_motorista_endpoint(motorista: Motorista):
    try:
        return criar_motorista(motorista.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
