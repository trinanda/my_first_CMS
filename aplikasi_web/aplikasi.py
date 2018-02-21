from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


def bikin_aplikasi():
    objek_flask = Flask(__name__)

    objek_flask.config.from_pyfile('settings.py')

    from aplikasi_web.models import database, Page, Post

    database.init_app(objek_flask)

    admin = Admin(objek_flask, name='Administrator', template_mode='bootstrap3')
    admin.add_view(ModelView(Page, database.session))

    @objek_flask.route('/')
    @objek_flask.route('/index')
    def index():
        halaman_depan = 'Hello'
        return render_template('about.html', HALAMAN_DEPAN=halaman_depan, TITLE='Homepage')

    @objek_flask.route('/about')
    def about():
        halaman = Page.query.filter_by(id=4).first()
        judul = Page.query.filter_by(id=1).first()

        return render_template('about.html', TITLE=judul.title, HALAMAN_DEPAN=halaman.content)

    return objek_flask