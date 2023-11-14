from flask import request,jsonify
from app import app


# Rota para comprar títulos
@app.route('/purchase_titulos', methods=['POST'])
def purchase_titulos():
    data = request.json
    # Lógica para processar a compra de títulos
    # Integração com APIs de investimento em títulos
    return jsonify({'message': 'Compra de títulos processada com sucesso'})