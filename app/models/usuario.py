from app.infra.database import db, ma



class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    saldo = db.Column(db.Float, nullable=False)
    telefone = db.Column(db.String(11), nullable=False)

    def __init__(self, nome, email, senha, saldo, telefone):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.saldo = saldo
        self.telefone = telefone


# Esquema de usuário para serialização com Marshmallow
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

user_schema = UserSchema()
users_schema = UserSchema(many=True)