from database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'  # Ensure this matches the MySQL table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  

class Goal(db.Model):
    __tablename__ = 'goal'  # Matches the MySQL table name
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  

class Group(db.Model):
    __tablename__ = 'user_groups'  # Matches the MySQL table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  

class Task(db.Model):
    __tablename__ = 'tasks'  # Matches the MySQL table name
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.id'), nullable=False)  # Foreign key referencing 'goal'




