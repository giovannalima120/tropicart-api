class Vaga:

    idAtual = 1
    vagas = []

    def __init__ (self, titulo, descricao, local, data):
        self.id = Vaga.idAtual
        self.titulo = titulo
        self.descricao = descricao
        self.local = local
        self.data = data
        