from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Configurações do banco de dados
user = 'nexums'
password = 'Mje07072003.'
host = 'db-invest.cqac9w6q6iaq.us-east-2.rds.amazonaws.com'
port = '5432'
database = 'db_invest'

def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nexums:Mje07072003.@db-invest.cqac9w6q6iaq.us-east-2.rds.amazonaws.com:5432/db_invest'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
