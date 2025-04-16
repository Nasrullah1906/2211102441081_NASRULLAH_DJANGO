 DJANGO_PROJECT
Fitur Website
HOME
Menampilkan halaman utama dari website

Dashboard
Menampilkan laporan grafis, manajemen data, serta informasi penting dalam tampilan visual yang informatif dan responsif.

Langkah Menjalankan Proyek


HOME - Menampilkan Halaman Utama dari website.
Dashboard - Menampilkan laporan grafis, manajemen informasi, dan data-data.
Cara Menjalankannya:

Buka Command Prompt (CMD)

Tekan Win + R, lalu ketik cmd dan tekan Enter.
Masuk ke Folder Tempat Proyek Akan Dibuat

Gunakan perintah cd untuk berpindah ke direktori tempat kamu ingin membuat proyek. Contoh:
cd nama_folder
Buat Virtual Environment

Gunakan perintah berikut untuk membuat virtual environment:
py -m venv .venv
Aktifkan Virtual Environment

Setelah membuat virtual environment, aktifkan dengan perintah berikut:
.venv\Scripts\activate


Install Django dengan menggunakan pip:
pip install django

Setelah instalasi selesai, buat migration dengan perintah:
python manage.py makemigrations
Migrate Database

Setelah migration dibuat, lakukan migrate ke database dengan perintah:
python manage.py migrate
Jalankan Server

Terakhir, jalankan server Django dengan perintah:
python manage.py runserver
