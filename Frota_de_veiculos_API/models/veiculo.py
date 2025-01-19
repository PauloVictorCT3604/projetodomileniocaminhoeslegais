from pydantic import BaseModel
from typing import Optional

class Veiculo(BaseModel):
    id: str
    placa: str
    modelo: str
    categoria: str
    status: str  # "disponível", "em trânsito", "em manutenção"
    base: str
    nome_motorista: Optional[str]