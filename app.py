from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def chat():
  

@app.route("/hello-world")
def hello_world():
    return "<p>Hello, World!</p>"
