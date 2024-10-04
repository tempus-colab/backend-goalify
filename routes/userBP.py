from flask import Blueprint
from controllers.userController import save, login


user_blueprint = Blueprint('userBP', __name__)


user_blueprint.route('/userS', methods=['POST'])(save)
user_blueprint.route('/login', methods=['POST'])(login)


