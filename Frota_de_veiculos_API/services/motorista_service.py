from dao.motorista_dao import buscar_motorista, adicionar_motorista

def criar_motorista(motorista):
    if buscar_motorista(motorista['id']):
        raise ValueError("ID do motorista já existe")
    adicionar_motorista(motorista)
    return motorista
