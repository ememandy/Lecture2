from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []
#empty lists of notes to store the notes that will be saved
#also a global variable

@app.route("/", methods=["GET", "POST"])
def index():
    #if session.get("notes") is None: it initializes note so that it doesnt keep disappearing when you add new notes
        #session["notes"] = [] this is just to show that the notes made will be specific to a user's Session
    #line 20 becomes session["notes"].append(note)
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("index.html", notes=notes)
