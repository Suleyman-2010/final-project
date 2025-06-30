from flask import Flask, jsonify, request

from connection_manager import connection

api = Flask(__name__)
DATABASE = ".users.db"


@api.get("/users")
def get_users():
    with connection(DATABASE) as cursor:
        return cursor.execute("SELECT * FROM users").fetchall(), 200


@api.post("/add_user")
def add_user():
    with connection(DATABASE) as cursor:
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?)", request.get_json())
    return "", 201


if __name__ == "__main__":
    api.run(port=5001)
