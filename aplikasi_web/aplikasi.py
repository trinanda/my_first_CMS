from flask import Flask


def bikin_aplikasi():
    objek_flask = Flask(__name__)

    @objek_flask.route('/')
    def pertama():
        return 'hello'

    return objek_flask