from flask import Flask, render_template


def bikin_aplikasi():
    objek_flask = Flask(__name__)

    objek_flask.config.from_pyfile('settings.py')

    from aplikasi_web.models import database, Page, Post

    database.init_app(objek_flask)

    @objek_flask.route('/')
    @objek_flask.route('/index')
    def index():
        halaman_depan = 'Hello'
        halaman_depan2 = 'Python Flask'
        return render_template('about.html', HALAMAN_DEPAN=halaman_depan, HALAMAN_DEPAN_2=halaman_depan2)

    @objek_flask.route('/about')
    def about():
        halaman = Page.query.filter_by(id=1).first()

        return render_template('about.html', HALAMAN_DEPAN=halaman.title)

    return objek_flask