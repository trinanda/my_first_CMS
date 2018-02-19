# my_first_CMS
This my first CMS using Python-flask

### 1. Main module
    1.1 import objek Flask, and others
    1.2 Make a function to store object aplication that you created 
    1.3 call __main__ object from flask, store it to a variable and dont forget to return it
    1.4 panggil file settings dengan variable objek Flask
        *-*. objek_flask.config.from_pyfile('settings.py')
    1.5 import what you'll need from models
    1.6 then insert your variable_flask_objek to database using *init_app()*
        *-* ini berfungsi untuk saling menghubungkan aplikasi dengan models(tables pada database)
    1.5 Buat route
    1.6 Make a function,and return what you will need e.g render template
        *-* pada function ini masukan apa saja yang ingin ditampilkan pada webpage
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
         *-*. server -build host:port --tampilkan-log --reload_jika_ada_perubahan "package.module:function()"
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
        #2. Jadikan base-template dengan jinja2:
            *-* {% block content %}
            *-* {% endblock %}
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

### 6. Alembic Configurations
    6.1 initialize alembic init
    6.2 go to alembic.ini file, then config on sqlalchemy.url
        #*# sqlalchemy.url function is a url to conect alembic to the database via SQLAlchemy
    6.3 On folder you have initialize on above, go to env.py, then config on target_metadata
        #*# as you can see on that file, you need to create new module that called models.py, function for this file is to create table to database
        #*# the imported will be not found, so..you must interact with interpreter
        #*# the way is, import sys module, then call path "path" list, and the "append" the package that you store your models
        
