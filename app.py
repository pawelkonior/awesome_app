from datetime import datetime
from random import randint, shuffle

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Witaj użytkowniku!"


@app.route("/hello/<username>")
def name(username):
    return username


@app.route("/time")
def get_time():
    return str(datetime.time(datetime.now()))


@app.route("/date")
def get_date():
    return str(datetime.date(datetime.now()))


@app.route("/licz/<int:a>/<int:b>", methods=["GET"])
def add(a, b):
    return str(a + b)


@app.route("/losuj")
def random_3():
    # digits = []
    #
    # for d in range(3):
    #     digits.append(str(randint(0, 9)))
    #
    # return ", ".join(digits)
    return ", ".join([str(randint(0, 9)) for _ in range(3)])


@app.route("/lotek")
def lotto():
    # digits = []
    #
    # while len(digits) <= 6:
    #     digit = str(randint(1, 49))
    #     if digit not in digits:
    #         digits.append(digit)
    #
    # return " - ".join(digits)
    digits = list(range(1, 50))
    shuffle(digits)
    return " - ".join(str(d) for d in digits[:6])


@app.route("/kontakt", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        first_name = request.form.get("firstName")
        return render_template("confirmation.html", first_name=first_name)
    return render_template("form.html")


operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: a / b,
    "*": lambda a, b: a * b,
    "%": lambda a, b: a % b,
}


@app.route('/calc', methods=["GET", "POST"])
def calculate():
    result = ''

    if request.method == "POST":
        operation = request.form.get("operation")

        try:
            digit1 = float(request.form.get("digit1"))
            digit2 = float(request.form.get("digit2"))
        except ValueError:
            return render_template("calculator.html", message="Podaj poprawne liczby, przyjacielu!")

        result = operations.get(operation)(digit1, digit2)

    return render_template("calculator.html", result=result)


@app.route("/method", methods=["GET", "POST"])
def check_method():
    if request.method == "POST":
        return "Wysłałeś POST"
    return "Wysłałeś GET"

