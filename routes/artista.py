from flask import Blueprint, request, jsonify
from services.artista_services import *

artista_bp = Blueprint("artistas", __name__)

@artista_bp.route("/usuarios", methods=["POST"])
def criar():
    dados = request.json
    novo_usuario = criar_usuario(dados)
    return jsonify(novo_usuario), 201