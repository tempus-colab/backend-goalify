from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Group, db

groups_bp = Blueprint('groups', __name__)

@groups_bp.route('/', methods=['GET'])
@jwt_required()
def get_groups():
    groups = Group.query.all()
    return jsonify([{'name': g.name, 'id': g.id} for g in groups]), 200

@groups_bp.route('/', methods=['POST'])
@jwt_required()
def create_group():
    data = request.get_json()
    user_id = get_jwt_identity()
    new_group = Group(name=data['name'], user_id=user_id)
    db.session.add(new_group)
    db.session.commit()
    return jsonify(message="Group created"), 201


