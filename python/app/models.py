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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), index=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    suggester_username = db.Column(db.String(16))
    up_votes = db.Column(db.Integer)
    down_votes = db.Column(db.Integer)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
