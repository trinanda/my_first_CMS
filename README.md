# my_first_CMS
This my first CMS using Python-flask

### 1. Konfigurasi Docker
    1.1. Dockerfile
         #1. Tentukan versi,image(sistem operasi yang akan digunakan)
         #2. Yang memanage / maintenance aplikasi
         #3. BUAT variable ENVIRONMENT untuk menentukan dimana aplikasi akan di install di dalam docker
         #4. Tentukan dimana default directory akan terbuka ketika masuk ke dalam docker
         #5. COPY semua file requirements.txt ke dalam docker
         #6. Kemudian install semua package yang tercantum di dalam requirements.txt yang berada didalam docker
    1.2. Docker-compose.yml
        #1. Tentukan versi docker-compose yang akan digunakan
        #2. Buat nama service nya
        #3. Build docker image+semua perintah yang berada pada dockerfile
        #4. Masukan command yang digunakan untuk menjalankan server
            *-* server -build host:port --tampilkan-log --reload_jika_ada_perubahan "package.module:function()"
        #5. Mount current directory ke dalam (target/docker)
            *-* Jika ada perubahan pada file local/yang di host, maka akan otomatis dikirim ke dalam docker
        #6. Spesifikasikan ports aplikasi yang berada di host/local dan juga port aplikasi yang di dalam docker
        