from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello!" #the headline variable is created in py but is manipulated in the html file
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)
