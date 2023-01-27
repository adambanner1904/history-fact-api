from flask import Flask, redirect, url_for, render_template, request
from api_request import get_info

app = Flask(__name__)


@app.route("/")
@app.route("/start-here")
def home():
    return render_template("index.html", content="Testing")


@app.route("/data/", methods=['POST', "GET"])
def data():
    if request.method == "GET":
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == "POST":
        form_data = request.form
        info = get_info(**{'text': form_data['text'], 'year': form_data['year'],
                           'month': form_data['month'], 'day': form_data['day']})


        return render_template("data.html", form_data=form_data, info = info)


if __name__ == "__main__":
    app.run(debug=True)
