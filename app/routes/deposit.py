from flask import Blueprint,Flask, request, jsonify
import stripe

app = Flask(__name__)

deposit_blueprint = Blueprint('deposit', __name__)

@deposit_blueprint.route('/deposit', methods=['POST'])
def deposit():
    amount = request.json.get("amount")
    currency = request.json.get("currency")
    card_number = request.json.get("card_number")
    exp_month = request.json.get("exp_month")
    exp_year = request.json.get("exp_year")
    cvc = request.json.get("cvc")
    description = request.json.get("description")

    try:
        payment_intent = stripe.PaymentIntent.create(
            amount = amount,
            currency = currency,
            payment_method_types = ["card"],
            payment_method_data = {
                "card": {
                    "number": card_number,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": cvc
                }
            },
            description = description
        )
        return jsonify({
            "client_secret": payment_intent.client_secret
        }), 200
    except stripe.error.CardError as e:
        return jsonify({
            "error": e.error.message
        }), 400
