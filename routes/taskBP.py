from flask import Blueprint
from controllers.taskController import add_task, get_tasks_for_goal, update_task, delete_task



task_routes = Blueprint('task_routes', __name__)

task_routes.route('/task/<int:goal_id>/tasks', methods=['POST'])(add_task)
task_routes.route('/task/<int:goal_id>/tasks', methods=['GET'])(get_tasks_for_goal)
task_routes.route('/task/<int:goal_id>/tasks/<int:task_id>', methods=['PUT'])(update_task)
task_routes.route('/task/<int:goal_id>/tasks/<int:task_id>', methods=['DELETE'])(delete_task)
