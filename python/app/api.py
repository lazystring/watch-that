from flask import Blueprint
from flask import request
from flask import jsonify
from flask_json import json_response
from flask_socketio import emit, join_room, leave_room

from app import db, socketio
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

    # TODO: Encrypt the group.id.
    return json_response(group_id=group.id)

@socketio.on('join_group')
def handle_join_group(data):
    username = data['username']
    group_id = data['group_id']

    group = db.session.query(Group).get(group_id)
    if group is None:
        handle_error(response_name='join_group_response',
                     error='Group does not exist')

    join_room(group_id)
    user = User(username=username, group_id=group_id)
    db.session.add(user)
    db.session.commit()

    response = group.serialize()

    emit('join_group_response', response, room=group_id)

def handle_error(response_name, error):
    emit(response_name, {'error': error})
