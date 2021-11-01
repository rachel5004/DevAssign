from urlcutter import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(6), unique=True, nullable=False)
    shortcut = db.Column(db.String(255), unique=True)
    create_date = db.Column(db.DateTime(), nullable=False)