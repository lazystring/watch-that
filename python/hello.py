from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Not much of an index page.'    
