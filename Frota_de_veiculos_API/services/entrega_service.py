from dao.entrega_dao import buscar_entrega, adicionar_entrega

def criar_entrega(entrega):
    if buscar_entrega(entrega['id']):
        raise ValueError("ID da entrega já existe")
    adicionar_entrega(entrega)
    return entrega
