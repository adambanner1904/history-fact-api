from flask import Flask, redirect, url_for, render_template, request
from api_request import get_info

app = Flask(__name__)


@app.route("/")
@app.route("/start-here")
def home():
    return render_template("index.html", content="Testing")


@app.route("/form1")
def form():
    return render_template("form1.html")

if __name__ == "__main__":
    app.run(debug=True)
