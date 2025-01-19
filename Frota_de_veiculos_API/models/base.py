from pydantic import BaseModel
from typing import List

class Base(BaseModel):
    id: str
    nome: str
    veiculos: List[str]  # IDs dos veículos
    motoristas: List[str]  # IDs dos motoristas
