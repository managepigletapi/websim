from flask import Flask, render_template
from slotsim import *
from botsim import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
