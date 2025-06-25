class Empresa:
    idAtual = 1
    empresas = []

    def __init__ (self, username, nome, email, senha, local, cnpj, descricao):
        self.id = Empresa.idAtual
        self.username = username
        self.nome = nome
        self.email = email
        self.senha = senha
        self.local = local
        self.cnpj = cnpj
        self.descricao = descricao