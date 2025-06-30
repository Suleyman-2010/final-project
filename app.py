import requests
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


def get_users():
    return requests.get("http://127.0.0.1:5001/users").json()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        info_names = ["name", "surname", "email", "phone_number"]
        infos = [request.form[name] for name in info_names]
        requests.post("http://127.0.0.1:5001/add_user", json=infos)
        return redirect("/")
    return render_template("index.html", users=get_users())


if __name__ == "__main__":
    app.run(debug=True)
