import unittest
from flask_testing import TestCase
from flask_socketio import SocketIOTestClient

from app import create_app, socketio, db
from app.models import Group, Video

class AppTest(TestCase):

    def create_app(self):
        return create_app('testing')

    def setUp(self):
        self.socketiotest = SocketIOTestClient(app=self.app, socketio=socketio)
        self.socketiotest.connect()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_group(self):
        api_route = '/api/v1.0/create_group'
        form_data = dict(
            groupname='test_group',
            username='test_user'
        )

        response = self.client.post(api_route, data=form_data)
        self.assert200(response)

        self.assertIn('group_id', response.json)
        group_id = response.json['group_id']

        group = db.session.query(Group).get(group_id)
        self.assertIsNotNone(group)

    def test_join_group(self):
        groupname = 'test_groupname'
        username = 'test_username'

        group = Group(name=groupname)
        db.session.add(group)
        db.session.commit()

        video = Video(title='test_video',
                      url='https://www.youtube.com/watch?v=test',
                      suggester_username='test_suggester',
                      up_votes=1,
                      down_votes=0,
                      group_id=group.id)

        db.session.add(video)
        db.session.commit()

        self.socketiotest.emit('join_group', {
            'username': username,
            'group_id': group.id
        })

        responses = self.socketiotest.get_received()
        self.assertNotEqual(len(responses), 0)

        self.assertEqual(responses[0]['name'], 'join_group_response')
        response = responses[0]['args'][0]
        self.assertNotIn('error', response)

        group = db.session.query(Group).get(group.id)
        db_users = group.users.all()
        response_users = response['users']
        response_videos = response['videos']

        self.assertEqual(len(db_users), 1)
        self.assertEqual(len(response_users), 1)
        self.assertEqual(len(response_videos), 1)

        self.assertEqual(response['id'], group.id)
        self.assertEqual(response_users[0]['id'], db_users[0].id)
        self.assertEqual(response_videos[0]['id'], video.id)

    def test_suggest_video(self):
        groupname = 'test_groupname'
        username = 'test_username'
        title = 'test_title'
        url = 'https://___.test-url.___'

        group = Group(name=groupname)
        db.session.add(group)
        db.session.commit()

        self.socketiotest.emit('join_group', {
            'username': 'test_username',
            'group_id': group.id
        })

        self.socketiotest.emit('suggest_video', {
            'url': url,
            'title': title,
            'suggester_username': username,
            'group_id': group.id
        })

        responses = self.socketiotest.get_received()
        self.assertNotEqual(len(responses), 0)

        self.assertEqual(responses[1]['name'], 'suggest_video_response')
        response = responses[1]['args'][0]

        video = db.session.query(Video).get(response['id'])
        self.assertIsNotNone(video)

    def test_pause_video(self):
        group = Group(name='test_group')
        db.session.add(group)
        db.session.commit()

        self.socketiotest.emit('join_group', {
            'username': 'test_username',
            'group_id': group.id
        })

        self.socketiotest.emit('pause_video', {
            'group_id':group.id
        })

        responses = self.socketiotest.get_received()

        self.assertNotEqual(len(responses), 0)
        self.assertEqual(responses[1]['name'], 'pause_video_response')

    def test_play_video(self):
        group = Group(name='test_group')
        db.session.add(group)
        db.session.commit()

        self.socketiotest.emit('join_group', {
            'username': 'test_username',
            'group_id': group.id
        })

        self.socketiotest.emit('play_video', {
            'group_id':group.id
        })

        responses = self.socketiotest.get_received()

        self.assertNotEqual(len(responses), 0)
        self.assertEqual(responses[1]['name'], 'play_video_response')

if __name__ == '__main__':
    unittest.main()
