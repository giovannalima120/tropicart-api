from flask import Flask
from routes.artista import artista_bp
from routes.empresa import empresa_bp
from routes.vaga import vaga_bp

app = Flask(__name__)

app.register_blueprint(artista_bp)
app.register_blueprint(empresa_bp)
app.register_blueprint(vaga_bp)

if __name__ == "__main__":
    app.run(debug=True)