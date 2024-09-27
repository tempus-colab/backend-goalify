from database import db
from models.user import User
from sqlalchemy import select

def login(username, password): 
    query = select(User).where(User.username == username)
    user = db.session.execute(query).scalar_one_or_none() 
    if user and user.password == password:
    
        response = {
            "status":"success",
            "message":"Successfully Logged In",
        }
        return response
    else:
        response = {
            "status": "fail",
            "message": "Invalid username or password"
        }
        return response


def save(user_data):
    
    new_user = User(name=user_data['name'], email=user_data['email'], password=user_data['password'], phone=user_data['phone'], username=user_data['username'])
    db.session.add(new_user)
    db.session.commit()

    db.session.refresh(new_user)
    return new_user
