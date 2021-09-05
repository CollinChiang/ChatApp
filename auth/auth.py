from utils.file_write import FileWrite
from flask import Blueprint, request, render_template, redirect, session
from flask_socketio import Namespace
from werkzeug.security import check_password_hash, generate_password_hash
from database.models import db, User
from string import ascii_letters, digits, punctuation, whitespace
from datetime import datetime

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

        if not verify_username(username):
            FileWrite.write("[AUTH] Invalid Username.")  # TODO REMOVE
            return redirect("/login")

        if not verify_password(password):
            FileWrite.write("[AUTH] Invalid Password.")  # TODO REMOVE
            return redirect("/login")

        user = User.query.filter_by(name=username).first()
        if user is None:
            FileWrite.write("[AUTH] Invalid Username.")  # TODO REMOVE
            return redirect("/login")
        
        if not check_password_hash(user.password, password):
            FileWrite.write("[AUTH] Invalid Password.")  # TODO REMOVE
            return redirect("/login")
        
        session["user_id"] = user.id

        return redirect("/")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth/register.html")

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        confirm_password = request.form["confirm_password"].strip()

        if not verify_username(username):
            FileWrite.write("[AUTH] Invalid Username.")  # TODO REMOVE
            return redirect("/register")

        user = User.query.filter_by(name=username).first()
        if user is not None:
            FileWrite.write("[AUTH] Non-Unique Username.")  # TODO REMOVE
            return redirect("/register")

        if not verify_password(password):
            FileWrite.write("[AUTH] Invalid Password.")  # TODO REMOVE
            return redirect("/register")

        if password != confirm_password:
            FileWrite.write("[AUTH] Incorrect Password.")  # TODO REMOVE
            return redirect("/register")

        user = User()
        user.name = username
        user.password = generate_password_hash(password)
        user.created_by = datetime.now()
        db.session.add(user)
        db.session.commit()

        return redirect("/login")


@auth_bp.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    if request.method == "GET":
        return render_template("auth/reset_password.html")

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()
        confirm_password = request.form["confirm_password"].strip()

        if not verify_username(username):
            FileWrite.write("[AUTH] Invalid Username.")  # TODO REMOVE
            return redirect("/reset_password")

        user = User.query.filter_by(name=username).first()
        if user is None:
            FileWrite.write("[AUTH] Invalid Username.")  # TODO REMOVE
            return redirect("/reset_password")

        if not verify_password(password):
            FileWrite.write("[AUTH] Invalid Password.")  # TODO REMOVE
            return redirect("/reset_password")
        
        if password != confirm_password:
            FileWrite.write("[AUTH] Incorrect Password.")  # TODO REMOVE
            return redirect("/reset_password")
        
        user.password = generate_password_hash(password)
        db.session.commit()

        return redirect("/login")


def verify(text: str, key: list):
    if text == "":
        return False

    for char in text:
        if char not in key:
            return False
    return True


def verify_username(text: str):
    key = ascii_letters + digits + whitespace
    return verify(text, key)


def verify_password(text: str):
    key = ascii_letters + digits + ascii_letters + digits + punctuation + whitespace
    return verify(text, key)
