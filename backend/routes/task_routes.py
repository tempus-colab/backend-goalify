from flask import Blueprint, jsonify, request
from models import db, Task, Goal
from utils import serialize_model

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/goals/<int:goal_id>/tasks', methods=['POST'])
def add_task(goal_id):
    goal = Goal.query.get(goal_id)
    
    if not goal:
        return jsonify({'message': 'Goal not found'}), 404
    
    data = request.json
    new_task = Task(
        goal_id=goal_id,
        task_description=data['task_description'],
        due_date=data['due_date'],
        status=data['status']
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'Task created successfully!'}), 201

@task_routes.route('/goals/<int:goal_id>/tasks', methods=['GET'])
def get_tasks_for_goal(goal_id):
    goal = Goal.query.get(goal_id)

    if not goal:
        return jsonify({'message': 'Goal not found'}), 404

    organized_tasks = [
        {
            'Task ID': task.task_id,
            'Description': task.task_description,
            'Due Date': task.due_date.strftime('%Y-%m-%d'),
            'Status': task.status
        } 
        for task in goal.tasks
    ]

    return jsonify({
        'Goal': {
            'Goal ID': goal.goal_id,
            'Title': goal.title,
            'Description': goal.description
        },
        'Tasks': organized_tasks
    })

@task_routes.route('/goals/<int:goal_id>/tasks/<int:task_id>', methods=['PUT'])
def update_task(goal_id, task_id):
    goal = Goal.query.get(goal_id)
    
    if not goal:
        return jsonify({'message': 'Goal not found'}), 404

    task = Task.query.get(task_id)
    
    if not task or task.goal_id != goal_id:
        return jsonify({'message': 'Task not found'}), 404

    data = request.json
    task.task_description = data['task_description']
    task.due_date = data['due_date']
    task.status = data['status']
    
    db.session.commit()

    return jsonify({'message': 'Task updated successfully!'}), 200

@task_routes.route('/goals/<int:goal_id>/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(goal_id, task_id):
    goal = Goal.query.get(goal_id)
    
    if not goal:
        return jsonify({'message': 'Goal not found'}), 404

    task = Task.query.get(task_id)
    
    if not task or task.goal_id != goal_id:
        return jsonify({'message': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted successfully!'}), 200



