from flask import Blueprint, request, jsonify
from services.empresa_services import *
from utils.erros import respostaErro

empresa_bp = Blueprint("empresas", __name__)

@empresa_bp.route("/empresas", methods=["GET"])
def listar():
    try:
        empresas = listarEmpresas()
        return jsonify(empresas), 200
    except Exception:
        return respostaErro(500, "ERRO_SERVIDOR", "Erro interno no servidor. Tente novamente mais tarde.")

@empresa_bp.route("/empresas/<int:id>", methods=["GET"])
def buscarPorId(id):
    if id <= 0:
        return respostaErro(400, "ID_INVALIDO", "O ID fornecido é inválido.")

    empresa = listarEmpresa(id)
    if not empresa:
        return respostaErro(404, "EMPRESA_NAO_ENCONTRADA", "Empresa não encontrada.")

    return jsonify(empresa.to_dict()), 200

@empresa_bp.route("/empresas", methods=["POST"])
def criar():
    dados = request.json
    campos_necessarios = ["username", "nome", "email", "senha", "local", "cnpj", "descricao"]

    if not dados or not all(campo in dados for campo in campos_necessarios):
        return respostaErro(400, "DADOS_INVALIDOS", "Dados inválidos.")

    if emailDuplicado(dados["email"]):
        return respostaErro(409, "EMAIL_DUPLICADO", "CNPJ ou email já cadastrados.")

    if cnpjDuplicado(dados["cnpj"]):
        return respostaErro(409, "CNPJ_DUPLICADO", "CNPJ ou email já cadastrados.")

    novaEmpresa = criarEmpresa(dados)
    return jsonify(novaEmpresa), 201

@empresa_bp.route("/empresas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.json
    campos_validos = ["username", "nome", "email", "senha", "local", "cnpj", "descricao"]

    if not dados or not any(campo in dados for campo in campos_validos):
        return respostaErro(400, "DADOS_INVALIDOS", "Os dados fornecidos são inválidos.")

    empresa = atualizarPorId(id, dados)
    if not empresa:
        return respostaErro(404, "EMPRESA_NAO_ENCONTRADA", "Empresa não encontrada.")

    return jsonify(empresa.to_dict()), 200

@empresa_bp.route("/empresas/<int:id>", methods=["DELETE"])
def deletar(id):
    if id <= 0:
        return respostaErro(400, "ID_INVALIDO", "O ID informado é inválido.")

    sucesso = deletarEmpresa(id)
    if not sucesso:
        return respostaErro(404, "EMPRESA_NAO_ENCONTRADA", "Empresa não encontrada.")

    return '', 204


