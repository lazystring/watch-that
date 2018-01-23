from app import db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    users = db.relationship('User',
                            backref='group',
                            cascade='all,delete',
                            lazy='dynamic')
    videos = db.relationship('Video',
                             backref='group',
                             cascade='all,delete',
                             lazy='dynamic')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'users': [user.serialize() for user in self.users.all()],
            'videos': [video.serialize() for video in self.videos.all()],
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'group_id': self.group_id,
        }

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    url = db.Column(db.String(120))
    suggester_username = db.Column(db.String(16))
    up_votes = db.Column(db.Integer)
    down_votes = db.Column(db.Integer)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'suggester_username': self.suggester_username,
            'up_votes': self.up_votes,
            'down_votes': self.down_votes,
            'group_id': self.group_id,
        }
