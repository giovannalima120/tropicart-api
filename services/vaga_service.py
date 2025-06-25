from models.vaga import Vaga

idAtual = 1
vagas = []

def gerarId():
    global idAtual
    idAtual += 1
    return idAtual

def listarVagas():
    lista = [u.to_dict() for u in vagas]
    return lista
    
def listarVagas(categoria=None, local=None):
    resultado = vagas 

    if categoria:
        resultado = [v for v in resultado if v.categoria.lower() == categoria.lower()]
    if local:
        resultado = [v for v in resultado if v.local.lower() == local.lower()]

    return resultado


def listarVaga(id):
    for u in vagas:
        if u.id == id:
            return u
    return None


def criarVaga(dados):
    vaga = Vaga(gerarId(), dados["titulo"], dados["descricao"], dados["local"], dados["data"], dados["empresaId"])
    vagas.append(vaga)
    return vaga.to_dict()


def deletarVagas(id):
    global vagas

    vagaEncontrada = listarVaga(id)  
    if vagaEncontrada:
        empresas = [u for u in empresas if u.id != id]   
        return True
    else: 
        return False  