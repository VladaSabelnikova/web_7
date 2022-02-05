import pathlib

from flask import Flask

from all_tasks.static.templates.temp import proposal


app = Flask(__name__)


@app.route('/')
def root():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    promotion_words = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!', 'Присоединяйся!'
    ]
    return '<br>'.join(promotion_words)


@app.route('/image_mars')
def image_mars():
    return pathlib.Path('static/html/img_mars.html').read_text()


@app.route('/promotion_image')
def promotion_image():
    return pathlib.Path('static/html/promotion_img.html').read_text()


@app.route('/astronaut_selection')
def astronaut_selection():
    return pathlib.Path('static/html/form.html').read_text()


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return proposal.format(planet_name)


def main():
    app.run(host='', port=8080)


if __name__ == '__main__':
    main()
