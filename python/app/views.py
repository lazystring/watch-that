from flask import Blueprint

app = Blueprint('app', __name__)

@app.route('/')
def index():
    return 'Not much of an index page.'
