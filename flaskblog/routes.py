from flask import render_template
from flaskblog import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/contents.html")
def contents():
    return render_template('contents.html')
