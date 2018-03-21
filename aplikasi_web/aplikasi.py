from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from aplikasi_web.views import PageModelView


def bikin_aplikasi():
    objek_flask = Flask(__name__)

    objek_flask.config.from_pyfile('settings.py')

    from aplikasi_web.models import database, Page, Menu

    database.init_app(objek_flask)

    admin = Admin(objek_flask, name='Administrator', template_mode='bootstrap3')
    admin.add_view(PageModelView(Page, database.session))
    admin.add_view(ModelView(Menu, database.session))

    @objek_flask.route('/')
    @objek_flask.route('/<url>')
    def index(url=None):
        page = Page()
        if url is not None:
            page = Page.query.filter_by(url=url).first()

        content = 'Homepage'
        if page is not None:
            content = page.content

        menu = Menu.query.order_by('order')

        return render_template('index.html', TITLE='Flask-CMS', CONTENT=content, menu=menu)

    return objek_flask