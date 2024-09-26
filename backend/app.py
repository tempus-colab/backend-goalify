from flask import Flask
from models import db
from config import Config
from routes.goal_routes import goal_routes  
from routes.task_routes import task_routes  

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


app.register_blueprint(goal_routes)
app.register_blueprint(task_routes)

@app.route('/')
def index():
    return "Server is running!"

if __name__ == '__main__':
    app.run(debug=True)


