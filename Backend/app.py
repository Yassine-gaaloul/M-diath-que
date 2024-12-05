from flask import Flask
from flask_cors import CORS
from routes.abonne_routes import abonne_bp
from routes.document_routes import livre_bp
from routes.emprunt_routes import emprunt_bp


app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})


# Enregistrer les blueprints
app.register_blueprint(abonne_bp, url_prefix='/api/')
app.register_blueprint(livre_bp, url_prefix='/api/' )
app.register_blueprint(emprunt_bp, url_prefix='/api/')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

