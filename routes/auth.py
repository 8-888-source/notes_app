from flask import Blueprint, render_template, request, redirect

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_user, logout_user, login_required

from extensions import db
from models.user import User


auth = Blueprint("auth", __name__)


# -------------------------
# REGISTRATION
# -------------------------
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # ❗ проверка на дубликат email
        user_exists = User.query.filter_by(email=email).first()

        if user_exists:
            return "❌ Этот email уже зарегистрирован"

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


# -------------------------
# LOGIN
# -------------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect("/notes")

        return "❌ Неверный email или пароль"

    return render_template("login.html")


# -------------------------
# LOGOUT
# -------------------------
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/login")