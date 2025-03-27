from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

app.config.from_object(Config)

# Import db after app is created
from models import db
db.init_app(app)

# Now import utils
from utils import convert_measurement

@app.route("/")
def home():
    return "Recipe Measurement Conversion API"

@app.route("/convert", methods=["POST"])
def convert():
    # Ensure request has JSON data
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    # Extract parameters
    ingredient_name = data.get("ingredient")
    amount = data.get("amount")
    from_unit = data.get("from_unit")
    to_unit = data.get("to_unit")

    # Validate required fields
    if not ingredient_name or amount is None or not from_unit or not to_unit:
        return jsonify({"error": "Missing required fields"}), 400

    # Perform the actual measurement conversion
    result = convert_measurement(ingredient_name, amount, from_unit, to_unit)

    return jsonify(result)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
