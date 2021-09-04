from FileWrite import FileWrite

from flask import Blueprint, request, render_template, redirect, session
from flask_socketio import Namespace

auth_bp = Blueprint("auth_bp", __name__, static_folder="static", template_folder="templates", static_url_path='/auth/static')


class AuthNamespace(Namespace):
    @staticmethod
    def on_connect():
        FileWrite.write(f"[AUTH] Client {request.sid} connected.")

    @staticmethod
    def on_disconnect():
        FileWrite.write(f"[AUTH] Client {request.sid} disconnected.")

    @staticmethod
    def on_authenticate(data):
        FileWrite.write(f"[AUTH] Client {request.sid} authenticated. With {data}.")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        session["username"] = username
        session["password"] = password

        return redirect("/")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth/register.html")

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        confirm_password = request.form["confirm_password"].strip()

        FileWrite.write(f"{username}, {password}, {confirm_password}")

        return redirect("/")


@auth_bp.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "GET":
        return render_template("auth/reset_password.html")

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        confirm_password = request.form["confirm_password"].strip()

        FileWrite.write(f"{username}, {password}, {confirm_password}")
        
        return redirect("/")
