from dao.veiculo_dao import buscar_veiculo, adicionar_veiculo

def criar_veiculo(veiculo):
    if buscar_veiculo(veiculo['id']):
        raise ValueError("ID do veículo já existe")
    adicionar_veiculo(veiculo)
    return veiculo