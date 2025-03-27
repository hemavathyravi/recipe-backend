import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/recipe_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
