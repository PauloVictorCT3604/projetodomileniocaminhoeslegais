from fastapi import APIRouter, HTTPException
from models.base import Base
from services.base_service import criar_base

roteador = APIRouter()

@roteador.post("/bases", response_model=Base)
def criar_base_endpoint(base: Base):
    try:
        return criar_base(base.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
