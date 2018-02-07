# my_first_CMS
This my first CMS using Python-flask

### 1. Main module
    1.1 import objek Flask
    1.2 Buat sebuah fungsi untuk menampung objek aplikasi, dont forget to return it
    1.3 panggil objek __main__ flask
    1.4 Buat route
    1.5 Make a function,and return what you will need i.e render template
    
    
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
         *-*. Buat nama service nya
         *-*. Build docker image+semua perintah yang berada pada dockerfile
         *-*. Masukan command yang digunakan untuk menjalankan server
         *-*. server -build host:port --tampilkan-log --reload_jika_ada_perubahan "package.module:function()"
         *-*. Mount current directory ke dalam (target/docker)
         *-*. Jika ada perubahan pada file local/yang di host, maka akan otomatis dikirim ke dalam docker
         *-*. Spesifikasikan ports aplikasi yang berada di host/local dan juga port aplikasi yang di dalam docker
         *-*. ------------------------------------
         *-*. Buat service baru untuk postgresql
         *-*. tentukan versi image yang akan digunakan
         *-*. buat environment untuk menampung username dan password
         *-*. buat volumes akan di mount ke mana, defaultnya 'var/lib/postgresql/data'
         *-*. buat ports postgre, host:docker
### 3. Templates
    3.1 index.html
        #1. Cari templates yang sesuai, masukan scriptnya ke file index
        