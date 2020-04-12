# Terminal:
# export FLASK_APP=app.py && python3 -m flask run

from flask import Flask, render_template, request, redirect, url_for, session
from mbta_helper import find_stop_near

app = Flask(__name__)

app.secret_key = "SuperSecretKey"

@app.route('/',methods=['POST','GET'])
def index():
    if request.method =='POST':
        session["place"] = request.form["place"]
        return redirect(url_for("nearest"))
    else:
        return render_template("index.html")

@app.route("/nearest")
def nearest():
    try:
        text = find_stop_near(session["place"])
        return render_template("place.html", text = text)
    except:
        return render_template('error.html')