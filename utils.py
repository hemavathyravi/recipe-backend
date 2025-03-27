"""from models import db, Ingredient

def convert_measurement(ingredient_name, quantity):
    ingredient = Ingredient.query.filter_by(name=ingredient_name).first()
    if not ingredient:
        return {"error": "Ingredient not found"}

    weight = quantity * ingredient.density * 236.588  # Convert cups to grams
    return {"ingredient": ingredient_name, "grams": round(weight, 2)}
"""

# utils.py

# Ingredient density lookup table (grams per cup)
INGREDIENT_DENSITIES = {
    "flour": 120,  # 1 cup = 120g
    "sugar": 200,  # 1 cup = 200g
    "butter": 227, # 1 cup = 227g
    "milk": 240,   # 1 cup = 240g
    "honey": 340,  # 1 cup = 340g
    "cocoa powder": 100  # 1 cup = 100g
}

# Conversion factors
CUP_TO_ML = 240
CUP_TO_TBSP = 16
CUP_TO_TSP = 48

def convert_measurement(ingredient, amount, from_unit, to_unit):
    """
    Convert baking measurements based on ingredient density and unit conversion.
    """

    # Ensure ingredient exists in database
    if ingredient.lower() not in INGREDIENT_DENSITIES:
        return {"error": "Ingredient not found in database"}

    density = INGREDIENT_DENSITIES[ingredient.lower()]  # Get density in grams per cup

    # Convert input to grams first
    if from_unit == "cups":
        amount_in_grams = amount * density
    elif from_unit == "grams":
        amount_in_grams = amount  # Already in grams
    elif from_unit == "ml":
        amount_in_grams = (amount / CUP_TO_ML) * density
    elif from_unit == "tbsp":
        amount_in_grams = (amount / CUP_TO_TBSP) * density
    elif from_unit == "tsp":
        amount_in_grams = (amount / CUP_TO_TSP) * density
    else:
        return {"error": "Invalid source unit"}

    # Convert grams to target unit
    if to_unit == "grams":
        converted_amount = amount_in_grams
    elif to_unit == "cups":
        converted_amount = amount_in_grams / density
    elif to_unit == "ml":
        converted_amount = (amount_in_grams / density) * CUP_TO_ML
    elif to_unit == "tbsp":
        converted_amount = (amount_in_grams / density) * CUP_TO_TBSP
    elif to_unit == "tsp":
        converted_amount = (amount_in_grams / density) * CUP_TO_TSP
    else:
        return {"error": "Invalid target unit"}

    return {"converted_amount": round(converted_amount, 2)}

