from flask import Flask, render_template


def bikin_aplikasi():
    objek_flask = Flask(__name__)

    @objek_flask.route('/')
    def pertama():
        return render_template("index.html")

    return objek_flask