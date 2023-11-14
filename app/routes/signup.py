from flask import Flask, request, jsonify, Blueprint
from ..models.usuario import Usuario
from ..models.usuario import user_schema
from firebase_admin import credentials, firestore
import firebase_admin
from firebase_admin import auth
from app.infra.database import db




cred = credentials.Certificate("C:/Users/MASNNO/Documents/FIAP/invest-nexums-firebase-adminsdk-4dtxy-4d72b9c011.json")
firebase_admin.initialize_app(cred)

db_firestore = firestore.client()

signup_blueprint = Blueprint('signup', __name__)

@signup_blueprint.route('/signup', methods=['POST'])
def signup():
    # Obter as informações do usuário a partir do corpo da requisição
    nome = request.json['nome']
    email = request.json['email']
    senha = request.json['senha']
    saldo = request.json['saldo']
    telefone = request.json['telefone']

    # Cadastrar o usuário no Firebase Authentication
    try:
        user = auth.create_user(
            email=email,
            password=senha,
            display_name=nome
        )
    except Exception as e:
        return jsonify({'message': f'{e}'}), 409

    # Cadastrar o usuário no banco de dados local
    new_user = Usuario(
        nome=nome,
        email=email,
        senha=senha,
        saldo=saldo,
        telefone=telefone
    )
    db.session.add(new_user)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({'message': 'Erro ao cadastrar usuário no banco de dados local'}), 500

    return jsonify({'message': 'Usuário cadastrado com sucesso'}), 201


@signup_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = Usuario.query.get(user_id)
    if user:
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        saldo = request.json['saldo']
        telefone = request.json['telefone']
        user.nome = nome
        user.email = email
        user.senha = senha
        user.saldo = saldo
        user.telefone = telefone
        db.session.commit()
        return user_schema.jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

@signup_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Usuario.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'})
    else:
        return jsonify({'message': 'User not found'}), 404
