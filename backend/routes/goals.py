from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models import Goal

goals = Blueprint('goals', __name__)

@goals.route('/', methods=['POST'])
@jwt_required()
def create_goal():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    new_goal = Goal(
        title=data['title'],
        completed=data.get('completed', False),
        user_id=user_id
    )
    
    db.session.add(new_goal)
    db.session.commit()
    
    return jsonify({
        'id': new_goal.id,
        'title': new_goal.title,
        'completed': new_goal.completed,
        'user_id': new_goal.user_id
    }), 201

@goals.route('/', methods=['GET'])
@jwt_required()
def get_goals():
    user_id = get_jwt_identity()
    goals = Goal.query.filter_by(user_id=user_id).all()
  
    return jsonify([{
        'id': goal.id,
        'title': goal.title,
        'completed': goal.completed,
        'user_id': goal.user_id
    } for goal in goals]), 200
