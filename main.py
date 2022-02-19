from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sum/<num1>/<num2>")
def addition(num1, num2):
    sum = int(num1) + int(num2)
    return render_template("calculator.html", sum=sum)


@app.route("/users")
def users():
    people = [{"id": 1, "name": "Mark", "moto": "Mark my words"},
              {"id": 2, "name": "Jonas", "moto": "Jonines yra gerai"},
              {"id": 3, "name": "Ugnius", "moto": "Viskas vistiek sudegs"}
              ]
    type = ""
    return render_template("users.html", people=people, type=type)


@app.route("/calculator", methods=["GET", "POST"])
def normal_addition():
    the_sum = 0
    if request.method == "POST":
        num1 = int(request.form['number1'])
        num2 = int(request.form['number2'])
        the_sum = num1 + num2

    return render_template("normal_calc.html", sum=the_sum)


@app.route("/isitchristmas")
def checker():
    time = str(datetime.date(datetime.now()))
    christmas = f"{str(datetime.year)}-12-25"
    value = "Jo" if (time == christmas) else "ne"
    return render_template("checker.html", data=value)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
