from flask import Blueprint, jsonify
from app.models.usuario import Usuario
from ..models.usuario import users_schema



get_routes = Blueprint('get_routes', __name__)

# Rota para buscar todos os usuários
@get_routes.route('/users', methods=['GET'])
def get_users():
    usuarios = Usuario.query.all()
    return users_schema.jsonify(usuarios)
