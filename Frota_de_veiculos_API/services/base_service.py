from dao.base_dao import buscar_base, adicionar_base

def criar_base(base):
    if buscar_base(base['id']):
        raise ValueError("ID da base já existe")
    adicionar_base(base)
    return base