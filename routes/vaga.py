from flask import Blueprint, request, jsonify
from services.vaga_services import *
from utils.erros import respostaErro

vaga_bp = Blueprint("vagas", __name__)

@vaga_bp.route("/vagas", methods=["GET"])
def listarOuFiltrar():
    try:
        categoria = request.args.get("categoria")
        local = request.args.get("local")

        if categoria and local:
            vagasFiltradas = filtrarVagas(categoria, local)
            if vagasFiltradas:
                return jsonify([v.to_dict() for v in vagasFiltradas]), 200
            else:
                return '', 204
        else:
            vagas = listarVagas()
            return jsonify(vagas), 200
    except ValueError:
        return respostaErro(400, "FILTRO_INVALIDO", "Os parâmetros de filtro são inválidos.")
    except Exception:
        return respostaErro(500, "ERRO_SERVIDOR", "Erro interno no servidor. Tente novamente mais tarde.")

@vaga_bp.route("/vagas/<int:id>", methods=["GET"])
def buscarPorId(id):
    if id <= 0:
        return respostaErro(400, "ID_INVALIDO", "ID fornecido é inválido.")

    vaga = buscarVagaPorId(id)
    if not vaga:
        return respostaErro(404, "VAGA_NAO_ENCONTRADA", "Vaga não encontrada.")

    return jsonify(vaga.to_dict()), 200

@vaga_bp.route("/vagas", methods=["POST"])
def criar():
    dados = request.json
    camposNecessarios = ["titulo", "descricao", "categoria", "local", "empresaId"]

    if not dados or not all(campo in dados for campo in camposNecessarios):
        return respostaErro(400, "DADOS_INVALIDOS", "Dados inválidos.")

    if not isinstance(dados["empresaId"], int) or dados["empresaId"] <= 0:
        return respostaErro(401, "NAO_AUTORIZADO", "Empresa não autenticada.")

    novaVaga = criarVaga(dados)
    return jsonify(novaVaga), 201

@vaga_bp.route("/vagas/<int:id>", methods=["DELETE"])
def deletar(id):
    if id <= 0:
        return respostaErro(400, "ID_INVALIDO", "ID fornecido é inválido.")

    sucesso = deletarVaga(id)
    if not sucesso:
        return respostaErro(404, "VAGA_NAO_ENCONTRADA", "Vaga não encontrada.")

    return '', 204


