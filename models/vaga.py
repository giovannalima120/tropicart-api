class Vaga:

    def __init__ (self, id, titulo, descricao, local, categoria, empresaId):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.local = local
        self.categoria = categoria
        self.empresaId = empresaId
    
    def to_dict(self):
        return{
            "id" : self.id,
            "titulo" : self.titulo,
            "descricao": self.descricao,
            "local" : self.local,
            "categoria": self.categoria,
            "empresaId": self.empresaId
        }

