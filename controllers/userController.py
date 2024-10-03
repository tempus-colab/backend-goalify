from flask import request, jsonify
from models.user import User
from marshmallow import ValidationError
from caching import cache
from mysql.connector import Error
from services import userService

#user Login
def login():
    try:
        credentials = request.json
        token = userService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'messages':'Invalid payload, expecting username and password'}), 401
    
    if token:
        return jsonify(token), 200
    else:
        return jsonify({'messages':'Invalid username or password'}), 401

#saving user to the database 
def save(): 
    try:
        user_data = User.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    user_saved = User.save(user_data)
    return User.jsonify(user_data), 201