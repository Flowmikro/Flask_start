import sqlite3
import os
from flask import Flask, render_template, flash, request, session, redirect, url_for, abort, g

# render_template - чтобы templates подгружал
# flash это типа ответ юзеру на взаимодействие с интерфейсом

# конфигурация
DATABASE = '/tmp/flsite.db'
DEBUG = True
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'
USERNAME = 'admin'
PASSWORD = '123'

app = Flask(__name__)
app.config.from_object(__name__)  # загружаем конфигурацию

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsite.db')))  # путь к БД


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


# manu = [
#     {'name': 'Установка', 'url': 'install-flask'},
#     {'name': 'Приложение', 'url': 'start-app'},
#     {'name': 'Контакты', 'url': 'contact'},
# ]


def get_db():  # соединение с БД
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):  # закрываем соединение с БД
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.route('/')  # с помощью декоратора прописываем url
def index():
    db= get_db()
    return render_template('index.html', menu=[])
#
#
# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         if len(request.form['username']) > 2:  # если имя больше 2 символов, теперь прописать условие в contact.html
#             flash('Отправлено')
#         else:
#             flash('Ошибка')
#     return render_template('contact.html')
#
#
# @app.route('/login', methods=['GET', 'POST'])  # прописываем регистрацию
# def login():
#     if 'userLogged' in session:  # исправляем синтаксис
#         return redirect(url_for('profile', username=session['userLogged']))
#     elif request.method == 'POST' and request.form['username'] == 'islam' and request.form['psw'] == '1234':
#         session['userLogged'] = request.form['username']
#         return redirect(url_for('profile', username=session['userLogged']))  # исправляем опечатку
#     return render_template('login.html')
#
#
# @app.route('/pofile/<username>')  # динамический url
# def profile(username):  # передаем аргумент
#     if 'userLogged' not in session or session['userLogged'] != username:
#         abort(401)
#
#     return f'Имя: {username}'  # например:   http://127.0.0.1:5000/pofile/islam -> Имя: islam
#
#
# # @app.route('/info')
# # def info():
# #     return '<h1>Инфо о сайте</h1>'  # так не вариант делать, по это templates делаем
#
# @app.errorhandler(404)  # ловим ошибку 404
# def page_not_fount(error):
#     return render_template('page404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
