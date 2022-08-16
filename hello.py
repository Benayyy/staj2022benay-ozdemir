from cProfile import run
from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello,World!</p>"
Flask --app hello run


