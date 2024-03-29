from flask import Blueprint
from flask import request
from flask_json import json_response
from flask_socketio import emit, join_room, leave_room

from app import db, socketio
from .models import User, Group, Video

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

@socketio.on('suggest_video')
def handle_suggest_video(data):
    video = Video(
        url=data['url'],
        title=data['title'],
        suggester_username=data['suggester_username'],
        up_votes=1,
        down_votes=0,
        group_id=data['group_id']
    )
    db.session.add(video)
    db.session.commit()

    response = video.serialize()

    emit('suggest_video_response', response, room=data['group_id'])

@socketio.on('pause_video')
def handle_pause_video(data):
    group_id = data['group_id']
    group = db.session.query(Group).get(group_id)
    if group is None:
        handle_error(response_name='pause_video_response',
                     error='Group does not exist')
    emit('pause_video_response', {}, room=group_id)

@socketio.on('play_video')
def handle_play_video(data):
    group_id = data['group_id']
    group = db.session.query(Group).get(group_id)
    if group is None:
        handle_error(response_name='play_video_response',
                     error='Group does not exist')
    emit('play_video_response', {}, room=group_id)

def handle_error(response_name, error):
    emit(response_name, {'error': error})
