""""""
from src import db


class PlayerStats(db.Model):  # add examined rooms
    id = db.Column(db.Integer, primary_key=True, unique=True)
    level = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    shoes = db.Column(db.Integer, nullable=False)
