from flask import Flask
from flask.cli import FlaskGroup
from environs import Env
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from route import app_route

env = Env()
app = Flask(__name__)
app.register_blueprint(app_route)
app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')

class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)
