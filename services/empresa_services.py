from models.empresa import Empresa

idAtual = 0
empresas = []

def gerarId():
    global idAtual
    idAtual += 1
    return idAtual

def listarEmpresas():
    lista = [u.to_dict() for u in empresas]
    return lista
    

def listarEmpresa(id):
    if not isinstance(id, int) or id <= 0:
        return None
    for empresa in empresas:
        if empresa.id == id:
            return empresa
    return None

def emailDuplicado(email):
    for empresa in empresas:
        if empresa.email == email:
            return True
    return False

def cnpjDuplicado(cnpj):
    for empresa in empresas:
        if empresa.cnpj == cnpj:
            return True
    return False


def criarEmpresa(dados):
    empresa = Empresa(gerarId(), dados["username"], dados["nome"], dados["email"], dados["senha"], dados["local"], dados["cnpj"], dados["descricao"])
    empresas.append(empresa)
    return empresa.to_dict()

def atualizarPorId(id, novosDados):
    empresaEncontrada = listarEmpresa(id)

    if empresaEncontrada:
       empresaEncontrada.username = novosDados.get("username", empresaEncontrada.username)
       empresaEncontrada.nome = novosDados.get("nome", empresaEncontrada.nome)
       empresaEncontrada.email = novosDados.get("email", empresaEncontrada.email)
       empresaEncontrada.senha = novosDados.get("senha", empresaEncontrada.senha)
       empresaEncontrada.local = novosDados.get("local", empresaEncontrada.local)
       empresaEncontrada.cnpj = novosDados.get("cnpj", empresaEncontrada.cnpj)
       empresaEncontrada.descricao = novosDados.get("descricao", empresaEncontrada.descricao)

    return empresaEncontrada

def deletarEmpresa(id):  
    global empresas
    empresaEncontrada = listarEmpresa(id)
    if empresaEncontrada:
        empresas = [e for e in empresas if e.id != id]
        return True
    return False
