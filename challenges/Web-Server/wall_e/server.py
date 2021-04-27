#!usr/bin/python3

from flask import Flask, render_template, send_from_directory
import signal
import sys
import os


HOST = ''
PORT = 80

app = Flask(__name__)


def keyboardInterruptHandler(signal, frame):
    sys.exit(0)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
          'favicon.ico',mimetype='image/vnd.microsoft.icon')


@app.route('/assets/css/<page>', methods=['GET'])
def css(page):
        return send_from_directory(os.path.join(app.root_path, 'static', 'css'), page)


@app.route('/assets/js/<page>', methods=['GET'])
def js(page):
        return send_from_directory(os.path.join(app.root_path, 'static', 'js'), page)


@app.route('/assets/fonts/<page>', methods=['GET'])
def fonts(page):
        return send_from_directory(os.path.join(app.root_path, 'static', 'fonts'), page)


@app.route('/assets/images/<page>', methods=['GET'])
def images(page):
        return send_from_directory(os.path.join(app.root_path, 'static', 'images'), page)


@app.route('/robots.txt', methods=['GET'])
def robots():
    return send_from_directory(os.path.join(app.root_path, 'resources'), 'robots.txt')


@app.route('/8059dd56-3bfb-11eb-adc1-0242ac120002/nothing-here.txt', methods=['GET'])
def flag():
    return send_from_directory(os.path.join(app.root_path, 'resources'), 'flag.txt')


@app.route('/<page>', methods=['GET'])
def pages(page):
    if page in ["about.html", "contact.html", "faq.html", "index.html", "shop.html"]:
        return render_template(page)
    else:
        return render_template("404.html")


def main():
    app.run('0.0.0.0', PORT, False)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, keyboardInterruptHandler)
    main()
