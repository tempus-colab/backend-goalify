from database import db
from datetime import date
from models  import task    


def add_task(goal_id, data):
    new_task = task(
        goal_id=goal_id,
        task_description=data['task_description'],
        due_date=date.fromisoformat(data['due_date']),
        status=data['status']
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return new_task


def get_tasks_for_goal(goal_id):
    tasks = task.query.filter_by(goal_id=goal_id).all()
    return tasks


def update_task(goal_id, task_id, data):
    task = task.query.get(task_id)
    if not task or task.goal_id != goal_id:
        return None
    task.task_description = data['task_description']
    task.due_date = date.fromisoformat(data['due_date'])
    task.status = data['status']
    db.session.commit()
    return task


def delete_task(goal_id, task_id):
    task = task.query.get(task_id)
    if not task or task.goal_id != goal_id:
        return None
    db.session.delete(task)
    db.session.commit()
    return task