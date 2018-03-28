# my_first_CMS
This my first CMS using Python-flask

### 1. Main module
    1.1 import objek Flask, and others what you'll need
    1.2 Make a function to store object aplication that you created 
    1.3 call __main__ object from flask, store it to a variable and dont forget to return it
    1.4 panggil file settings dengan variable objek Flask
        *-*. objek_flask.config.from_pyfile('settings.py')
    1.5 import what you'll need from models, such.. database.., page.., menu.. etc..
    1.6 then insert your variable_flask_objek to database using *init_app()*
        *-* ini berfungsi untuk saling menghubungkan aplikasi dengan models(tables pada database)
    1.7 make your flask-admin objek
        admin=Admin(your_flask_objek, name='your dashboard name', and template_mode='sampai pada saat aplikasi ini dibuat, flask-admin baru hanya support bootstrap3')
    1.8 for administrative views.., add model view, model view are form from our models (table)
        *-* for example: admin.add_view(PageModelView(table_from_models, db.sessions))
        *-* and other add_view that you'll need
    1.8 Buat route
        *-* for route.. you need to declare url that you called from model
            #*# format for this route is like this: @object_flask_name.route('/<url>')
    1.9 Make a function, and insert the an url argument, and the argument is None(None is equal to empty)
        *-* the function of the argmunet </url> // in the function is to memberi nilai url apapun, kosong bisa di handle, 
            and return what you will need e.g render template, etc..
        
        *-* pada function ini masukan apa saja yang ingin ditampilkan pada webpage, as an example:
        
        *-* and then store to a variable value(Class) from table(models) that you need
            e.g: page= Page(), this variable function is to make the Page class to be global variable
    
### 2. Docker Configurations
    2.1. Dockerfile
         *-*. Tentukan versi,image(sistem operasi yang akan digunakan)
         *-*. Yang memanage / maintenance aplikasi
         *-*. update sistem, lalu install libpq-dev (packge python untuk postgresql)
         *-*. BUAT variable ENVIRONMENT untuk menentukan dimana aplikasi akan di install di dalam docker
         *-*. Tentukan dimana default directory akan terbuka ketika masuk ke dalam docker
         *-*. COPY semua file requirements.txt ke dalam docker
         *-*. Kemudian install semua package yang tercantum di dalam requirements.txt yang berada didalam docker
    2.2. Docker-compose.yaml
         *-*. Tentukan versi docker-compose yang akan digunakan
         *-*. Buat nama service untuk aplikasi
         *-*. Build docker image+semua perintah yang berada pada dockerfile
         *-*. Masukan command yang digunakan untuk menjalankan server
            #*#. server (gunicorn) -build host:port --tampilkan-log --reload_jika_ada_perubahan "package.module:function()"
         *-*. Mount directory aplikasi yang di host(local) ke dalam (target/docker (aplikasi_docker)) 
            #*#. Jika ada perubahan pada file local/yang di host, maka akan otomatis dikirim ke dalam docker
         *-*. Spesifikasikan ports aplikasi yang berada di host/local dan juga port aplikasi yang di dalam docker
            #*# This must be same with server port on the above
         *-*. ------------------------------------
         *-*. Buat service baru untuk postgresql
         *-*. tentukan versi image yang akan digunakan
         *-*. buat environment untuk menampung username dan password
         *-*. buat volumes untuk/akan di mount/diletakkan ke mana data postgres akan di simpan, usualy di kenal dengan nama postgres and default it stored on 'var/lib/postgresql/data'
         *-*. buat ports postgre, host:docker
### 3. Templates
    3.1 base-template.html
        #1. Cari templates yang sesuai
        #2. Jadikan base-template dengan jinja2 pada bagian yang Anda butuhkan, ini biasanya berada pada element <main></main>:
            *-* {% block content %}
            *-* {% endblock %}
        #3. Kemudian pada element navigasi buat perulangan for dengan jinja2
            *-* {% for iterasi untuk elemen_dari_table_yang_ingin_dilakukan_perulangan %}
                    pada kasus ini, Anda perlu melakukan perulangan pada column URL dan title
                {% endfor %}
    3.2 template lain untuk me render ke base-template.html, e.g index.html:
        *-*. {% extends "base-template" %}
        *-*. {% block content %}
        *-*. {% endblock %}
        
    
### 4. settings.py
    *-* DEBUG = True
        #*# Langsung me reload jika ada perubahan pada kode
    *-* SQLALCHEMY_DATABASE_URI = 'driver://username:password@postgre_servicename_from_docker/database_name' 
        #*# To connec python with postgre
    *-* SQLALCHEMY_TRACK_MODIFICATIONS = ''
        #*# This will track modifications of objects, this requires extra memory and should be disabled(False) if not needed
    *-* SECRET_KEY = 'yourScreetKey'
        #*# this config you needed if you were using flask-admin
       
### 5. requirements.txt
    *-* flask
        A microfremwork for python, that can develop web aplication
    *-* gunicorn
        A Python WSGI HTTP server 
        #*# WSGI function is how to web server communicate with web aplication
    *-* psycopg2
        This is the most popular postgresql adapter for Python, this serves to communicated python with postgre
    *-* flask-sqlalchemy
        ORM package for python-flask, flask-sqlalchemy berfungsi untuk lebih mempermudah penggunaan sqlalchemy untuk flask
    *-* alembic
        this tools for migrations database, such.. adding column to table, etc..
    *-* flask-admin
        package fro customize your flask application back-end (CRUD)
    *-* flask-wtf
        package for ...
    
### 6. Alembic Configurations
    6.1 initialize alembic init
    6.2 go to alembic.ini file, then config on sqlalchemy.url
        #*# sqlalchemy.url function is a url to conect alembic to the database via SQLAlchemy
    6.3 On folder you have initialize on above, go to env.py, then config on target_metadata
        #*# as you can see on that file, you need to create new module that called models.py, function for this file is to create table to database
        #*# the imported will be not found, so..you must interact with interpreter
        #*# the way is, import sys module, then call path "path" list, and then "append" the package that you store your models
        
### 7. Prototype Application
    7.1 if your aplications still prototype, you don't need versions file migrations as much
        #*# but if your aplication on deploy or sudah di serahkah ke tangan user, maka perubahan data perlu di kembangkan sedikit demi sedikit
        #*# maka dari itu, buat lah file reset_migrations.sh
            #*# on this file, first.. * you need to downgrade base on alembic
                                      * then remove versions files on alembic directory
                                      * alembic revision (initialize your db)
                                      * and then upgrade your db to the new versions
                                      
### 8. Models
    8.1 first thing on module models you must declare SQLAlchemy() object
    8.2 and then create class to create table to the database, and on this class call your Model from SQLAlchemy object that you have created on the above
        then add column what you'll need, e.g id, title, name, etc..
    8.3 in this case, you created two table, Page and Menu
    8.4 on the table menu, you must add foreign key on column ID to table Page
    8.5 then add relationship to table page ....
    
### 9. Views
    9.1 on this module yo can add ckEditor for WYSIWYG, this function for edit column content on your dashboard (admin view)
    9.2 you can also ....