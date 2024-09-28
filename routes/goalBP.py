from flask import Blueprint, request, jsonify
from controllers.goalController import add_goal, get_goals, update_goal, delete_goal

goal_routes = Blueprint('goals', __name__)

goal_routes.route('/goals', methods=['POST'])(add_goal)
goal_routes.route('/goals', methods=['GET'])(get_goals)
goal_routes.route('/goals/<int:goal_id>', methods=['PUT'])(update_goal)
goal_routes.route('/goals/<int:goal_id>', methods=['DELETE'])(delete_goal)




