from flask import Flask
from environs import Env
from models import db

from route import app_route

env = Env()
app = Flask(__name__)
app.register_blueprint(app_route)
app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')

db.init_app(app)
