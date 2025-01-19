import json

ARQUIVO_VEICULOS = "veiculos.json"

# Carregar dados do arquivo
try:
    with open(ARQUIVO_VEICULOS, "r") as f:
        veiculos = json.load(f)
except FileNotFoundError:
    veiculos = []

# Salvar dados no arquivo
def salvar_veiculos():
    with open(ARQUIVO_VEICULOS, "w") as f:
        json.dump(veiculos, f, indent=4)

def buscar_veiculo(veiculo_id: str):
    return next((v for v in veiculos if v['id'] == veiculo_id), None)

def adicionar_veiculo(veiculo):
    veiculos.append(veiculo)
    salvar_veiculos()

def remover_veiculo(veiculo):
    veiculos.remove(veiculo)
    salvar_veiculos()