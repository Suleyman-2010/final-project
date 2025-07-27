from flask import Flask, Response, jsonify, redirect, render_template, request

from connection_manager import connection

app: Flask = Flask(__name__)
DATABASE = ".users.db"
info_names = ("name", "surname", "email", "phone_number")


def get_users():
    with connection(DATABASE) as cursor:
        return cursor.execute("SELECT * FROM users").fetchall()


def add_user(info) -> None:
    with connection(DATABASE) as cursor:
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?)", info)


@app.route("/user/<int:user>", methods=["GET", "DELETE"])
def user(user):
    with connection(DATABASE) as cursor:
        if request.method == "DELETE":
            cursor.execute("DELETE FROM users LIMIT 1 OFFSET ?", (user,))
            return Response(status=204)

        result = cursor.execute(
            "SELECT * FROM users LIMIT 1 OFFSET ?", (user,)
        ).fetchone()

        if result is None:
            return jsonify({"error": "User not found"}), 404

        return jsonify(dict(zip(info_names, result))), 200


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        info = [request.form[name] for name in info_names]
        add_user(info)
        return redirect("/")
    return render_template("index.html", users=get_users())
