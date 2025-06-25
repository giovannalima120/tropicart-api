class Vaga:

    def __init__ (self, id, titulo, descricao, local, data):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.local = local
        self.data = data
    
    def to_dict(self):
        return{
            "id" : self.id,
            "titulo" : self.titulo,
            "descricao": self.descricao,
            "local" : self.local,
            "data": self.data
        }

