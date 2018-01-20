from flask import Blueprint
from flask import request
from flask_json import json_response

from app import db
from .models import User, Group

api = Blueprint('api', __name__)

@api.route('/api/v1.0/create_group', methods=['POST'])
def create_group():
    # TODO: Add validation.
    username = request.form['username']
    groupname = request.form['groupname']

    group = Group(name=groupname)
    db.session.add(group)
    db.session.commit()

    user = User(username=username, group_id=group.id)
    db.session.add(user)
    db.session.commit()

    # TODO: Encrypt the group.id.
    return json_response(group_id=group.id)
