from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate  # ✅ Import Flask-Migrate
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)  # ✅ Load database config
CORS(app)  # ✅ Enable CORS

# Initialize Database
from models import db  # ✅ Import db correctly
db.init_app(app)  # ✅ Initialize db
migrate = Migrate(app, db)  # ✅ Initialize Flask-Migrate

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
    unit = data.get("unit")  # ✅ Changed to match frontend

    # Validate required fields
    if not ingredient_name or amount is None or not unit:
        return jsonify({"error": "Missing required fields"}), 400

    # Perform the actual measurement conversion
    result = convert_measurement(ingredient_name, amount, unit)

    return jsonify(result)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # ✅ Ensure tables are created
    app.run(debug=True)
