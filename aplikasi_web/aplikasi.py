from flask import Flask


def bikin_aplikasi():
    objek_flask = Flask(__name__)

    @objek_flask.route('/')
    def pertama():
        return 'hello world'

    return objek_flask