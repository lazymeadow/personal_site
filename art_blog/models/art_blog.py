from art_blog import db


class Post(db.Model):
    title = db.Column(db.String(32))
    published = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')


class Comment(db.Model):
    author = db.Column(db.String(64))
    published = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
