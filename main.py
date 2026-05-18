from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("teknoloji-bagimliligi.html")
@app.route("/info")
def info():
    return render_template("info.html")

app.run(debug=True)