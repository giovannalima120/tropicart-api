from flask import jsonify

def respostaErro(statusCodigo, erroCodigo, mensagem):
    return jsonify({
        "errorCode": erroCodigo,
        "message": mensagem
    }), statusCodigo
