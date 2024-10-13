import os

class ApplicationConfiguration:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///app.db'
    CACHE_TYPE =  os.environ.get('CACHE_TYPE') or 'SimpleCache'
    DEBUG = os.environ.get('ENV') != 'production'
