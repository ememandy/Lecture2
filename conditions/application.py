import datetime #python module for getting the current date

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    #new_year = True
    return render_template("index.html", new_year=new_year)