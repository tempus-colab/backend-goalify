from database import db
from models  import Goal
from datetime import date

def add_a_goal(data):
    new_goal = Goal(
        title=data['title'],
        description=data['description'],
        start_date=date.fromisoformat(data['start_date']),
        end_date=date.fromisoformat(data['end_date']),
        reminder_time=data['reminder_time']
    )
    
    db.session.add(new_goal)
    db.session.commit()
    
    return new_goal


def get_goals():
    goals = Goal.query.all()
    return goals


def get_goal(goal_id):
    goal = Goal.query.get(goal_id)
    return goal


def update_goal(goal_id, data):
    goal = Goal.query.get(goal_id)
    if not goal:
        return None
    goal.title = data['title']
    goal.description = data['description']
    goal.start_date = date.fromisoformat(data['start_date'])
    goal.end_date = date.fromisoformat(data['end_date'])
    goal.reminder_time = data['reminder_time']
    db.session.commit()
    return goal



def delete_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if not goal:
        return None
    db.session.delete(goal)
    db.session.commit()
    return goal








