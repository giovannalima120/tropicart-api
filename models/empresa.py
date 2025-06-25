class Empresa:

    def __init__ (self, id, username, nome, email, senha, local, cnpj, descricao):
        self.id = id
        self.username = username
        self.nome = nome
        self.email = email
        self.senha = senha
        self.local = local
        self.cnpj = cnpj
        self.descricao = descricao
    
    def to_dict(self):
        return{
            "id" : self.id,
            "username" : self.username,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "local" : self.local,
            "cnpj": self.cnpj,
            "descricao": self.descricao
        }