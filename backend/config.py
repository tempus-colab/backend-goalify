import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_jwt_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:newyork12@localhost/goalify'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
