import json

ARQUIVO_BASES = "bases.json"

# Carregar dados do arquivo
try:
    with open(ARQUIVO_BASES, "r") as f:
        bases = json.load(f)
except FileNotFoundError:
    bases = []

# Salvar dados no arquivo
def salvar_bases():
    with open(ARQUIVO_BASES, "w") as f:
        json.dump(bases, f, indent=4)

def buscar_base(base_id: str):
    return next((b for b in bases if b['id'] == base_id), None)

def adicionar_base(base):
    bases.append(base)
    salvar_bases()

def remover_base(base):
    bases.remove(base)
    salvar_bases()