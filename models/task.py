from database import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'tasks'
    task_id = db.Column(db.Integer, primary_key=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('goals.goal_id'), nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.Date)
    status = db.Column(db.String(100), default='pending')