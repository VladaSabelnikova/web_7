import pathlib

from flask import Flask

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


def main():
    app.run(host='', port=8080)


if __name__ == '__main__':
    main()
