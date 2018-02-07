# my_first_CMS
This my first CMS using Python-flask

### 1. Main module
    1.1 import objek Flask
    1.2 Buat sebuah fungsi untuk menampung objek aplikasi
    1.3 panggil objek __main__ flask, dont forget to return it
    1.4 panggil file settings dengan variable objek Flask
        *-*. objek_flask.config.from_pyfile('settings.py')
    1.5 Buat route
    1.6 Make a function,and return what you will need e.g render template
    
    
### 2. Konfigurasi Docker
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
         *-*. ------------------------------------
         *-*. Buat service baru untuk postgresql
         *-*. tentukan versi image yang akan digunakan
         *-*. buat environment untuk menampung username dan password
         *-*. buat volumes akan di mount ke mana, defaultnya 'var/lib/postgresql/data'
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
    4.1 DEBUG = True
        *-*. Langsung me reload jika ada perubahan pada kode
        