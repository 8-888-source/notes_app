from flask import Flask, render_template

from config import Config
from extensions import db, login_manager

from models.user import User
from models.note import Note

from routes.auth import auth
from routes.notes import notes


# создаём приложение
app = Flask(__name__)
app.config.from_object(Config)

# подключаем расширения
db.init_app(app)
login_manager.init_app(app)


# настройка Flask-Login
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# регистрируем blueprints
app.register_blueprint(auth)
app.register_blueprint(notes)


# создаём таблицы в БД
with app.app_context():
    db.create_all()


# главная страница (тест)
@app.route("/")
def home():
    return render_template('base.html')


# запуск сервера
if __name__ == "__main__":
    app.run(debug=True)