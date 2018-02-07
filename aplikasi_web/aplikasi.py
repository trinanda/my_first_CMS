from flask import Flask, render_template


def bikin_aplikasi():
    objek_flask = Flask(__name__)

    objek_flask.config.from_pyfile('settings.py')

    @objek_flask.route('/about')
    def pertama():
        halaman_depan = 'Hello'
        halaman_depan2 = 'Python Flask'
        return render_template('about.html', HALAMAN_DEPAN=halaman_depan, HALAMAN_DEPAN_2=halaman_depan2)

    @objek_flask.route('/')
    @objek_flask.route('/index')
    def index():
        halaman_depan = 'Welcome'
        halaman_depan2 = 'This CMS developed with Flask'
        return render_template('index.html', HALAMAN_DEPAN=halaman_depan, HALAMAN_DEPAN_2=halaman_depan2)

    return objek_flask