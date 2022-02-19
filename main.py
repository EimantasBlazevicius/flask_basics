from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/sum/<num1>/<num2>")
def another(num1, num2):
    sum = int(num1) - int(num2)
    return f"<h2>Hello, World from another page! {sum}</h2>"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
