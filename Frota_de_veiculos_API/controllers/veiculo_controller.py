from fastapi import APIRouter, HTTPException
from models.veiculo import Veiculo
from services.veiculo_service import criar_veiculo

roteador = APIRouter()

@roteador.post("/veiculos", response_model=Veiculo)
def criar_veiculo_endpoint(veiculo: Veiculo):
    try:
        return criar_veiculo(veiculo.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))