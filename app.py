from flask import Flask

app = Flask(__name__)

@app.route("/index.html")
def homepage():
    return render_template("index.html")

@app.route("/avd_details/<avd_id>")
def avd_details(avd_id):
    return 