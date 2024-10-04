from flask import Flask
from flask_cors import CORS
from database import db
from caching import cache
from routes.userBP import user_blueprint
from routes.taskBP import task_routes
from routes.goalBP import goal_routes
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name':"GOALIFY"})



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
    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app = create_app('DevelopmentConfig')
    blueprint_config(app)
    with app.app_context():
        db.create_all()

app.run(debug=True)  
