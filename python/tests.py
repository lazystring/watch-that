import unittest
from flask_testing import TestCase

from app import create_app, db
from app.models import Group

class AppTest(TestCase):

    def create_app(self):
        return create_app('testing')

    def setUp(self):
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

        users = group.users.all()
        self.assertEqual(len(users), 1)
        self.assertIsNotNone(users[0])
        self.assertEqual(users[0].username, form_data['username'])
        self.assertEqual(users[0].group_id, group_id)

if __name__ == '__main__':
    unittest.main()
