from pathlib import Path

from flask import (Flask, Response, redirect, render_template, request,
                   send_from_directory)

from connection_manager import connection

app = Flask(__name__)
DATABASE = "users.db"

users = []


def renew_users():
    with connection(DATABASE) as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()


renew_users()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        phone_number = request.form["phone-number"]
        with connection(DATABASE) as cursor:
            cursor.execute(
                "INSERT INTO users VALUES(?, ?, ?, ?)",
                (name, surname, email, phone_number),
            )
        renew_users()
        return redirect("/")
    print(users)
    return render_template("index.html", users=users)


@app.route("/favicon.ico")
def icon():
    static_dir = Path(__file__).parent / "static"
    return send_from_directory(
        static_dir, "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )
