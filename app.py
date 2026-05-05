from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/avd_details.html")
def avd_details():
    return render_template("avd_details.html")