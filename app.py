# flask run
from flask import Flask
from lib.foo import foo

app = Flask(__name__)

@app.route("/")
def index():
    return foo("ping")
