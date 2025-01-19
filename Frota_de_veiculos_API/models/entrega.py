from pydantic import BaseModel
from typing import Optional
from datetime import date

class Entrega(BaseModel):
    id: str
    origem: str
    destino: str
    tipo: str
    id_veiculo: Optional[str]
    data_saida: date
    data_chegada: Optional[date]
    status: str  # "em trânsito", "concluída"