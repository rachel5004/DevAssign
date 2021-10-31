from urlcutter import db

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortcut = db.Column(db.String(24), unique=True, nullable=False)
    shortcut = db.Column(db.String(255), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)