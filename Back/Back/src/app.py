import os
from flask import Flask
from flask_cors import CORS
from routes import configure_routes  # Importar las rutas desde routes.py
import vertexai  # Importar vertexai para inicializar el proyecto

app = Flask(__name__)
CORS(app)  # Habilitar CORS

# Configurar la ruta del archivo de credenciales JSON de Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\\Users\\dragn\\Escritorio\\Hackaton\\gcp-banorte-hackaton-team-38-ee1e96b2a6d6.json"

# Inicializar Vertex AI con las credenciales
vertexai.init(project="gcp-banorte-hackaton-team-38", location="us-central1")

# Configurar las rutas
configure_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
