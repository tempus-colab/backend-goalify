from flask import Flask
from flask_cors import CORS
from database import db
from caching import cache
from routes.userBP import user_blueprint
from routes.taskBP import task_routes
from routes.goalBP import goal_routes


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    cache.init_app(app)
    CORS(app)

    print('Running')

    return app

def blueprint_config(app):
    app.register_blueprint(goal_routes)
    app.register_blueprint(task_routes)
    app.register_blueprint(user_blueprint)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')
    blueprint_config(app)
    with app.app_context():
        db.create_all()

app.run(debug=True)  
