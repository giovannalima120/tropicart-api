from models.vaga import Vaga

idAtual = 0
vagas = []

def gerarId():
    global idAtual
    idAtual += 1
    return idAtual

def listarVagas():
    return [vaga.to_dict() for vaga in vagas]

def filtrarVagas(categoria, local):
    if not categoria or not local:
        return None
    resultado = [
        vaga for vaga in vagas
        if vaga.categoria.lower() == categoria.lower()
        and vaga.local.lower() == local.lower()
    ]
    return resultado

def buscarVagaPorId(id):
    for vaga in vagas:
        if vaga.id == id:
            return vaga
    return None

def criarVaga(dados):
    vaga = Vaga(
        gerarId(),
        dados["titulo"],
        dados["descricao"],
        dados["local"],
        dados["categoria"],
        dados["empresaId"]
    )
    vagas.append(vaga)
    return vaga.to_dict()

def deletarVaga(id):
    global vagas
    vaga = buscarVagaPorId(id)
    if vaga:
        vagas = [v for v in vagas if v.id != id]
        return True
    return False