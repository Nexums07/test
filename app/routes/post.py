from flask import Blueprint, Flask, request,jsonify
import firebase_admin
from firebase_admin import credentials





# Configuração do Firebase
cred = credentials.Certificate("C:/Users/MASNNO/Documents/FIAP/invest-nexums-firebase-adminsdk-4dtxy-4d72b9c011.json")
firebase_admin.initialize_app(cred)

# Configuração da aplicação Flask
app = Flask(__name__)



post_blueprint = Blueprint('post', __name__)

@post_blueprint.route('/users', methods=['POST'])
def login():
    email = request.json['email']
    senha = request.json['senha']




# Rota para comprar ações
@app.route('/comprar_acoes', methods=['POST'])
def comprar_acoes():
    data = request.json
    # Lógica para processar a compra de ações
    # Integração com APIs de investimento de ações
    return jsonify({'message': 'Compra de ações processada com sucesso'})

# Rota para comprar títulos
@app.route('/comprar_titulos', methods=['POST'])
def comprar_titulos():
    data = request.json
    # Lógica para processar a compra de títulos
    # Integração com APIs de investimento em títulos
    return jsonify({'message': 'Compra de títulos processada com sucesso'})

# Rota para comprar fundos mútuos
@app.route('/comprar_fundos_mutuos', methods=['POST'])
def comprar_fundos_mutuos():
    data = request.json
    # Lógica para processar a compra de fundos mútuos
    # Integração com APIs de investimento em fundos mútuos
    return jsonify({'message': 'Compra de fundos mútuos processada com sucesso'})

# Rota para comprar criptomoedas
@app.route('/comprar_criptomoedas', methods=['POST'])
def comprar_criptomoedas():
    data = request.json
    # Lógica para processar a compra de criptomoedas
    # Integração com APIs de investimento em criptomoedas
    return jsonify({'message': 'Compra de criptomoedas processada com sucesso'})
