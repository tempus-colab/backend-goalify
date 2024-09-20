from flask import Flask
from database import db  
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.goals import goals  # Correct import here
from routes.groups import groups_bp
from routes.stats import stats_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:newyork12@localhost/goalify_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret'

db.init_app(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return "App is running"

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(goals, url_prefix='/api/goals')  
app.register_blueprint(groups_bp, url_prefix='/api/groups')
app.register_blueprint(stats_bp, url_prefix='/api/stats')

if __name__ == "__main__":
    app.run(debug=True)

