from db import db


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.column(db.Text, nullable=False)
