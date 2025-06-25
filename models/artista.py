class Artista:
    idAtual = 1
    artistas = []

    def __init__ (self, username, nome, email, senha, dataNasc, local, biografia):
        self.id = Artista.idAtual
        self.username = username
        self.nome = nome
        self.email = email
        self.senha = senha
        self.dataNasc = dataNasc
        self.local = local
        self.biografia = biografia
        Artista.idAtual += 1
