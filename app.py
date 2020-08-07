from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="src")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/eu")
def eu():
    return render_template("eu.html")

@app.route("/itechdesk")
def stub():
    return render_template("itechdesk.html")

if __name__ == "__main__":
    app.run(debug=True)