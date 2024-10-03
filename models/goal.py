from database import db
from datetime import datetime  


class Goal(db.Model):
    __tablename__ = 'goals'
    goal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    reminder_time = db.Column(db.Time)

        
    tasks = db.relationship('Task', backref='goal', lazy=True, cascade="all, delete")