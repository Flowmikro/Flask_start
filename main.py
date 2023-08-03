from flask import Flask, render_template  # render_template - чтобы templates подгружал

app = Flask(__name__)


@app.route('/')  # с помощью декоратора прописываем url
def index():
    return render_template('index.html')


@app.route('/name/<username>')  # динамический url
def username(username):  # передаем аргумент
    return f'Имя: {username}'  # например:  http://127.0.0.1:5000/name/islam -> Имя: islam


# @app.route('/info')
# def info():
#     return '<h1>Инфо о сайте</h1>'  # так не вариант делать, по это templates делаем


if __name__ == '__main__':
    app.run(debug=True)
