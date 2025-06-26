from models.artista import Artista

idAtual = 1
artistas = []


def gerarId():
    global idAtual
    idAtual += 1
    return idAtual

def listarArtistas():
    lista = [u.to_dict() for u in artistas]
    return lista
    

def listarArtista(id):
    for u in artistas:
        if u.id == id:
            return u
    return None

def buscarUsername(artistaUsername):
    for artista in artistas:  
        if artista.username == artistaUsername:
            return artista
    return None

def emailDuplicado(email):
    for artista in artistas:
        if artista.email == email:
            return True
    return False


def criarArtista(dados):
    artista = Artista(gerarId(), dados["username"], dados["nome"], dados["email"], dados["senha"], dados["dataNasc"], dados["local"], dados["biografia"], dados["categoria"])
    artistas.append(artista)
    return artista.to_dict()

def atualizarPorId(id, novosDados):
    artistaEncontrado = listarArtista(id)

    if artistaEncontrado:
       artistaEncontrado.username = novosDados.get("username", artistaEncontrado.username)
       artistaEncontrado.nome = novosDados.get("nome", artistaEncontrado.nome)
       artistaEncontrado.email = novosDados.get("email", artistaEncontrado.email)
       artistaEncontrado.senha = novosDados.get("senha", artistaEncontrado.senha)
       artistaEncontrado.dataNasc = novosDados.get("dataNasc", artistaEncontrado.dataNasc)
       artistaEncontrado.local = novosDados.get("local", artistaEncontrado.local)
       artistaEncontrado.biografia = novosDados.get("biografia", artistaEncontrado.biografia)
       artistaEncontrado.categoria = novosDados.get("categoria", artistaEncontrado.categoria)

    return artistaEncontrado

def deletarArtista(id):
    global artistas

    artistaEncontrado = listarArtista(id)  
    if artistaEncontrado:
        artistas = [u for u in artistas if u.id != id]   
        return True
    else: 
        return False  
    

