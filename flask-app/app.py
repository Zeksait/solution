from flask import Flask
from environs import Env

env = Env()
app = Flask(__name__)

@app.route('/')
def index():
   return "ТЕСТ"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

#https://github.com/testdrivenio/flask-on-docker