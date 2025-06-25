class Artista:
   
    def __init__ (self, id, username, nome, email, senha, dataNasc, local, biografia, categoria):
        self.id = id
        self.username = username
        self.nome = nome
        self.email = email
        self.senha = senha
        self.dataNasc = dataNasc
        self.local = local
        self.biografia = biografia
        self.categoria = categoria


    def to_dict(self):
        return{
            "id" : self.id,
            "username" : self.username,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "dataNasc": self.dataNasc,
            "local" : self.local,
            "biografia": self.biografia,
            "categoria": self.categoria
        }
    