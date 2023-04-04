from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("test")
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
