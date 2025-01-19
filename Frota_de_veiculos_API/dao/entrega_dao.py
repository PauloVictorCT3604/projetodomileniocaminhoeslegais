import json

ARQUIVO_ENTREGAS = "entregas.json"

# Carregar dados do arquivo
try:
    with open(ARQUIVO_ENTREGAS, "r") as f:
        entregas = json.load(f)
except FileNotFoundError:
    entregas = []

# Salvar dados no arquivo
def salvar_entregas():
    with open(ARQUIVO_ENTREGAS, "w") as f:
        json.dump(entregas, f, indent=4)

def buscar_entrega(entrega_id: str):
    return next((e for e in entregas if e['id'] == entrega_id), None)

def adicionar_entrega(entrega):
    entregas.append(entrega)
    salvar_entregas()

def remover_entrega(entrega):
    entregas.remove(entrega)
    salvar_entregas()
