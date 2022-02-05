import pathlib
from flask import Flask, request

from all_tasks.static.templates.temp import proposal, result, open_file

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


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return result.format(nickname, level, rating)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():

    if request.method == 'GET':
        return pathlib.Path('static/html/load_photo.html').read_text()

    elif request.method == 'POST':
        content = request.files['file']

        file_name = content.filename
        file = pathlib.Path(f'static/img/{file_name}')
        file.write_bytes(content.stream.read())

        return open_file.format(file_name)


@app.route('/carousel')
def carousel():
    return pathlib.Path('static/html/carousel.html').read_text()


def main():
    app.run(host='', port=8080)


if __name__ == '__main__':
    main()
