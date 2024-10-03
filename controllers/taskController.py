from flask import request, jsonify
from models.task  import  Task
from models.goal import Goal
from marshmallow import ValidationError
from caching import cache       



def add_task(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'message': 'task not found'}), 404
    
    data = request.json
    new_task = Task(
    task_id=task_id,
        task_description=data['task_description'],
        due_date=data['due_date'],
        status=data['status']
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'Task created successfully!'}), 201



def get_tasks_for_goal(goal_id):
    goal = Goal.query.get(goal_id)

    if not goal:
        return jsonify({'message': 'task not found'}), 404

    organized_tasks = [
        {
            'Task ID': task.goal_id,
            'Description': task.task_description,
            'Due Date': task.due_date.strftime('%Y-%m-%d'),
            'Status': task.status
        } 
        for task in goal.tasks
    ]

    return jsonify({
        'goal': {
            'goal ID': goal.goal_id,
            'Title': goal.title,
            'Description': goal.description
        },
        'Tasks': organized_tasks
    })
    
    

def update_task(task_id):
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'message': 'task not found'}), 404

    task = Task.query.get(task_id)
    
    if not task or task.task_id != task_id:
        return jsonify({'message': 'Task not found'}), 404

    data = request.json
    task.task_description = data['task_description']
    task.due_date = data['due_date']
    task.status = data['status']
    
    db.session.commit()

    return jsonify({'message': 'Task updated successfully!'}), 200



def delete_task(task_id):
    task = task.query.get(task_id)
    
    if not task:
        return jsonify({'message': 'task not found'}), 404

    task = Task.query.get(task_id)
    
    if not task or task.task_id != task_id:
        return jsonify({'message': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted successfully!'}), 200