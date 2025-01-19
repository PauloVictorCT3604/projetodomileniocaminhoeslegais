import json

ARQUIVO_MOTORISTAS = "motoristas.json"

# Carregar dados do arquivo
try:
    with open(ARQUIVO_MOTORISTAS, "r") as f:
        motoristas = json.load(f)
except FileNotFoundError:
    motoristas = []

# Salvar dados no arquivo
def salvar_motoristas():
    with open(ARQUIVO_MOTORISTAS, "w") as f:
        json.dump(motoristas, f, indent=4)

def buscar_motorista(motorista_id: str):
    return next((m for m in motoristas if m['id'] == motorista_id), None)

def adicionar_motorista(motorista):
    motoristas.append(motorista)
    salvar_motoristas()

def remover_motorista(motorista):
    motoristas.remove(motorista)
    salvar_motoristas()