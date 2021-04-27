from app import db

class User(db.Model):

    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key=True)
    # author (string, unique, can't be null)
    author = db.Column(db.String(64), index=True, unique=True)
    # message (linkd to Messages table)
    message = db.relationship('Messages', backref='author', lazy='dynamic')
    # __repr__ function that outputs <User author>
    def __repr__(self):
        return f'<User {self.author}>'

class Messages(db.Model):

    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key=True)
    # message (string, not unique, can't be null)
    message = db.Column(db.String(256), index = True)
    # user_id link to id (int)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # __repr__ function that outputs <Message: MESSAGE_GOES_HERE>
    def __repr__(self):
        return f'<Message: {self.message}>'
