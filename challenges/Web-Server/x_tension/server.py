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


@app.route('/256c936a-fe91-4263-8373-c82ad1549ef5', methods=['GET'])
def decodeur():
    return render_template("decodeur.html")


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
          'favicon.ico',mimetype='image/vnd.microsoft.icon')


def main():
    app.run('0.0.0.0', PORT, False)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, keyboardInterruptHandler)
    main()
