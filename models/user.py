from database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'  # Ensure this matches the MySQL table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  
