from flask import Flask
from app.infra.database import configure_app
from app.routes.deposit import deposit_blueprint
from app.routes.signup import signup_blueprint
from app.infra.database import database

import stripe

# Configura a aplicação Flask
app = Flask(__name__)

# Configura o aplicativo usando a função configure_app
configure_app(app)

# Registra os blueprints
app.register_blueprint(deposit_blueprint)
app.register_blueprint(signup_blueprint)

stripe.api_key = "sk_test_51MwIB2LfQgtST3QsNSI0M5vh1crlAatCdvvDGGGGIMIRRgORAcBjR5l0VBFWCPxAmcgHgN6gEeH8YSHSNoXC9SBD002puBZROi"

# Roda a aplicação
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
