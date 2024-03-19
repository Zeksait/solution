from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    lang = db.Column(db.String(10))
    achievements = db.relationship('UserAchievement')
    
    def __repr__(self):
        return f"{self.username} ({self.lang})"


class UserAchievement(db.Model):
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), primary_key=True)
    achievement_id = db.Column(db.Integer(), db.ForeignKey('achievement.id'), primary_key=True)
    d_create = db.Column(db.String(128))
    user = db.relationship('User')
    achievement = db.relationship('Achievement')
    
    def __repr__(self):
        return f"{self.user} - {self.achievement}"


class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    points = db.Column(db.Integer)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f"{self.name} ({self.points})"
