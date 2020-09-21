from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Kelvin"

@app.route("/user/<username>")
def show_user(username):
    return 'Hello %s' % escape(username)
app.run(port=8080)