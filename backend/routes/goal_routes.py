from flask import Blueprint, jsonify, request
from models import db, Goal
from utils import serialize_goal, validate_goal_data

goal_routes = Blueprint('goal_routes', __name__)

@goal_routes.route('/goals', methods=['GET'])
def get_goals():
    goals = Goal.query.order_by(Goal.goal_id.asc()).all()

    organized_goals = []
    for goal in goals:
        serialized_goal = serialize_goal(goal)
        serialized_goal['tasks'] = [
            {
                'Task ID': task.task_id,
                'Description': task.task_description,
                'Due Date': task.due_date.strftime('%Y-%m-%d'),
                'Status': task.status
            } 
            for task in goal.tasks
        ]
        organized_goals.append({
            'Goal ID': serialized_goal['goal_id'],
            'Title': serialized_goal['title'],
            'Description': serialized_goal['description'],
            'Start Date': serialized_goal['start_date'],
            'End Date': serialized_goal['end_date'],
            'Reminder Time': serialized_goal['reminder_time'],
            'Tasks': serialized_goal['tasks']
        })

    return jsonify(organized_goals)

@goal_routes.route('/goals', methods=['POST'])
def add_goal():
    data = request.json

    error = validate_goal_data(data)
    if error:
        return jsonify({'message': error}), 400

    new_goal = Goal(
        title=data['title'],
        description=data['description'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        reminder_time=data['reminder_time']
    )
    db.session.add(new_goal)
    db.session.commit()

    return jsonify({'message': 'Goal created successfully!'}), 201

@goal_routes.route('/goals/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if not goal:
        return jsonify({'message': 'Goal not found'}), 404
    
    data = request.json
    goal.title = data['title']
    goal.description = data['description']
    goal.start_date = data['start_date']
    goal.end_date = data['end_date']
    goal.reminder_time = data['reminder_time']
    
    db.session.commit()

    return jsonify({'message': 'Goal updated successfully!'}), 200

@goal_routes.route('/goals/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    goal = Goal.query.get(goal_id)
    if not goal:
        return jsonify({'message': 'Goal not found'}), 404

    db.session.delete(goal)
    db.session.commit()

    return jsonify({'message': 'Goal deleted successfully!'}), 200





