from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)
# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de API desde la variable de entorno
api_key = os.getenv('API_KEY')

# Verificar que la clave de API esté presente
if not api_key:
    raise ValueError("La clave de API no está definida. Asegúrate de que el archivo .env contiene 'API_KEY'.")

# Configura la API de Gemini
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']
    response = model.generate_content(user_input)
    response_text = response.text
    return jsonify({'response_text': response_text})

if __name__ == '__main__':
    app.run(debug=True)
