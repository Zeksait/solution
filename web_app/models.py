from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True)
    lang = db.Column(db.String(10))

    def __str__(self):
        return f"{self.username} ({self.lang})"