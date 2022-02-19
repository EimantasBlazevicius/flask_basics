from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sum/<num1>/<num2>")
def addition(num1, num2):
    sum = int(num1) + int(num2)
    return render_template("calculator.html", sum=sum)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
