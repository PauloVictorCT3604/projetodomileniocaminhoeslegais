from pydantic import BaseModel

class Motorista(BaseModel):
    id: str
    nome: str
    idade: int
    cnh: str  # Categorias: A, B, AB, C, D, E
    status: str  # "disponível", "em entrega"
    base: str
