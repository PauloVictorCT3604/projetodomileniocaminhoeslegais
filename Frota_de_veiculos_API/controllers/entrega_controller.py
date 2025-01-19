from fastapi import APIRouter, HTTPException
from models.entrega import Entrega
from services.entrega_service import criar_entrega

roteador = APIRouter()

@roteador.post("/entregas", response_model=Entrega)
def criar_entrega_endpoint(entrega: Entrega):
    try:
        return criar_entrega(entrega.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))