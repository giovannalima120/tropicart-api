from flask import Blueprint, request, jsonify
from services.artista_services import *
from utils.erros import respostaErro

artista_bp = Blueprint("artistas", __name__)

@artista_bp.route("/artistas", methods=["POST"])
def criar():
    dados = request.json

    campos = ["username", "nome", "email", "senha", "dataNasc", "local", "biografia", "categoria"]
    if not all(campo in dados for campo in campos):
        return respostaErro(400, "DADOS_INVALIDOS", "Dados inválidos.")

    # ✅ Verificar duplicidade de e-mail (se esse método existir no modelo)
    if Artista.buscar_por_email(dados["email"]):
        return erro_response(409, "EMAIL_DUPLICADO", "Este email já está em uso.")

    try:
        novo_artista = criarArtista(dados)
        return jsonify(novo_artista), 201

    except Exception:
        return erro_response(500, "ERRO_SERVIDOR", "Erro interno no servidor. Tente novamente mais tarde.")