from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Goal, db

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/', methods=['GET'])
@jwt_required()
def get_stats():
    user_id = get_jwt_identity()
    total_goals = Goal.query.filter_by(user_id=user_id).count()
    completed_goals = Goal.query.filter_by(user_id=user_id, completed=True).count()
    streak = 281  # Example streak, can be dynamically calculated
    return jsonify({
        'total_goals': total_goals,
        'completed_goals': completed_goals,
        'streak': streak
    }), 200
