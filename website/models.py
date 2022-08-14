from turtle import title
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    title = db.Column(db.String(1000))
    topic = db.Column(db.String(1000))
    attendees = db.Column(db.String(100))
    raised_by = db.Column(db.String(100))
    actions_required = db.Column(db.String(100))
    actioned_by = db.Column(db.String(100))
    subsequent_information = db.Column(db.String(100))
    end_time = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    meetings = db.relationship("Meeting")
