from models.empresa import Empresa

idAtual = 1
empresas = []

def gerarId():
    global idAtual
    idAtual += 1
    return idAtual

def listarEmpresas():
    lista = [u.to_dict() for u in empresas]
    return lista
    

def listarEmpresa(id):
    for u in empresas:
        if u.id == id:
            return u
    return None

def buscarUsername(empresaUsername):
    for empresa in empresaUsername:
        if empresa.username == empresaUsername:
            return empresa
    return None

def criarEmpresa(dados):
    empresa = Empresa(gerarId(), dados["username"], dados["nome"], dados["email"], dados["senha"], dados["local"], dados["cnpj"], dados["descricao"])
    artistas.append(empresa)
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

def deletarArtista(id):
    global artistas

    empresaEncontrada = listarEmpresa(id)  
    if empresaEncontrada:
        empresas = [u for u in empresas if u.id != id]   
        return True
    else: 
        return False  