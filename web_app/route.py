from flask import Blueprint
from models import User

app_route = Blueprint('route', __name__)

@app_route.route('/')
def index():
   return str(User.query.all())
