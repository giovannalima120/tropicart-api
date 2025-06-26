from flask import Blueprint, request, jsonify
from services.artista_services import *
from utils.erros import respostaErro

artista_bp = Blueprint("artistas", __name__)

@artista_bp.route("/artistas/<int:id>", methods=["GET"])
def listarPorId(id):
    artista = listarArtista(id)
    if not artista:
        return respostaErro(404, "ARTISTA_NAO_ENCONTRADO", "O artista informado não foi encontrado.")
    return jsonify(artista.to_dict()), 200

@artista_bp.route("/artistas/username/<username>", methods=["GET"])
def buscarPorUsername(username):
    if not username:
        return respostaErro(400, "USUARIO_INVALIDO", "O usuário fornecido é inválido.")
    artista = buscarUsername(username)
    if not artista:
        return respostaErro(404, "ARTISTA_NAO_ENCONTRADO", "O artista informado não foi encontrado.")
    return jsonify(artista.to_dict()), 200

@artista_bp.route("/artistas", methods=["POST"])
def criar():
    dados = request.json
    campos_necessarios = ["username", "nome", "email", "senha", "dataNasc", "local", "biografia", "categoria"]

    if not dados or not all(campo in dados for campo in campos_necessarios):
        return respostaErro(400, "DADOS_INVALIDOS", "Dados inválidos.")

    if emailDuplicado(dados["email"]):
        return respostaErro(409, "EMAIL_DUPLICADO", "Este email já está em uso.")

    novoArtista = criarArtista(dados)
    return jsonify(novoArtista), 201

@artista_bp.route("/artistas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.json
    campos_validos = ["username", "nome", "email", "senha", "dataNasc", "local", "biografia", "categoria"]

    if not dados or not any(campo in dados for campo in campos_validos):
        return respostaErro(400, "DADOS_INVALIDOS", "Os dados são inválidos.")

    artista = atualizarPorId(id, dados)
    if not artista:
        return respostaErro(404, "ARTISTA_NAO_ENCONTRADO", "Artista não encontrado.")

    return jsonify(artista.to_dict()), 200

@artista_bp.route("/artistas/<int:id>", methods=["DELETE"])
def deletar(id):
    if not isinstance(id, int) or id <= 0:
        return respostaErro(400, "ID_INVALIDO", "O ID é inválido.")

    sucesso = deletarArtista(id)
    if not sucesso:
        return respostaErro(404, "ARTISTA_NAO_ENCONTRADO", "Artista não encontrado.")

    return '', 204
