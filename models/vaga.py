class Vaga:

    def __init__ (self, id, titulo, descricao, local, data, empresaId):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.local = local
        self.data = data
        self.empresaId = empresaId
    
    def to_dict(self):
        return{
            "id" : self.id,
            "titulo" : self.titulo,
            "descricao": self.descricao,
            "local" : self.local,
            "data": self.data,
            "empresaId": self.empresaId
        }

