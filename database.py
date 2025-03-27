from app import app
from models import db, Ingredient

def init_db():
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")

        # Insert default ingredient densities
        if not Ingredient.query.first():
            ingredients = [
                Ingredient(name="flour", density=0.593),
                Ingredient(name="sugar", density=0.845),
                Ingredient(name="butter", density=0.911),
            ]
            db.session.bulk_save_objects(ingredients)
            db.session.commit()
            print("Default ingredients added.")

if __name__ == "__main__":
    init_db()
