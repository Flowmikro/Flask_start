from flask import Flask, render_template, flash, request

# render_template - чтобы templates подгружал
# flash это типа ответ юзеру на взаимодействие с интерфейсом


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfq4gv34qhgbvqqqqqqqqba'
# секретный ключ типа как {% csrf_token %}
# значение придумываем сами

manu = [
    {'name': 'Установка', 'url': 'install-flask'},
    {'name': 'Приложение', 'url': 'start-app'},
    {'name': 'Контакты', 'url': 'contact'},
]


@app.route('/')  # с помощью декоратора прописываем url
def index():
    return render_template('index.html', menu=manu)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:  # если имя больше 2 символов, теперь прописать условие в contact.html
            flash('Отправлено')
        else:
            flash('Ошибка')
    return render_template('contact.html')


@app.route('/name/<username>')  # динамический url
def username(username):  # передаем аргумент
    return f'Имя: {username}'  # например:   http://127.0.0.1:5000/name/islam -> Имя: islam


# @app.route('/info')
# def info():
#     return '<h1>Инфо о сайте</h1>'  # так не вариант делать, по это templates делаем


if __name__ == '__main__':
    app.run(debug=True)
