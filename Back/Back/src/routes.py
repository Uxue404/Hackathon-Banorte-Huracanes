from flask import request, jsonify
from vertex import generate_investment_plan  # Importar la función de vertex.py

def configure_routes(app):
    # Ruta para generar el plan de inversión
    @app.route('/generate-plan', methods=['POST'])
    def generate_plan():
        try:
            # Obtener los datos enviados por el cliente (ej. Angular)
            request_data = request.get_json()

            # Los textos que se pasan al modelo
            text1 = request_data.get('text1')
            textsi_1 = "Eres un asesor financiero."
            #textsi_1 = request_data.get('textsi_1')

            # Llamar a la función de generación de Vertex AI
            response = generate_investment_plan(text1, textsi_1)

            # Retornar el plan generado
            return jsonify({"generated_plan": response}), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
