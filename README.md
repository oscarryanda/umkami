# UMKaMi

**_Disusun oleh : Oscar Ryanda Putra | 2306217765 | PBP F_**

## Tugas 2

### 1) Proses Pembuatan Projek Django

##### Check 1 : Membuat sebuah proyek Django baru

1. Buatlah sebuah direktory baru bernama `umkami` di komputer
2. Kemudian, buat juga _repository_ baru di Github bernama sama yaitu `umkami` dengan visibility _public_.
3. Dalam direktory baru tersebut, buka _command prompt_
4. Buatlah _virtual enviroment_ menggunakan python dengan command :
   ```bash
   python -m venv env
   ```
5. Lalu, aktifkan _virtual environement_ dengan command :
   ```bash
   env\Scripts\activate
   ```
6. _Virtual environment_ akan aktif yang ditandai (env) di awal baris input terminal
7. Buatlah file dengan nama `requirements.txt` di dalam direktori yang sama dan tambahkan beberapa _dependencies_ berikut di file tersebut :
   ```text
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
8. Melakukan instalansi _dependencies_ pada `requirements.txt` dengan command :
   ```python
   pip install -r requirements.txt
   ```
9. Buatlah proyek Django baru dengan nama `umkami` dengan command :
   ```bash
   django-admin startproject umkami .
   ```

- Note : Pastikan `.` tertulis dalam baris command

10. Ubahlah isi variabel `ALLOWED_HOSTS` di file `settings.py` dengan menambahkan kode berikut :
    ```python
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ...
    ```
11. Sebelumnya, pastikan terdapat file `manage.py` pada direktori yang aktif pada terminal kamu saat ini. Lalu, jalankan _server_ Django dengan command berikut :
    ```bash
    python manage.py runserver
    ```
12. Buka link [http://localhost:8000](http://localhost:8000/) pada browser dan pastikan muncul gambar roket yang menandakan bahwa Django berhasil diinstal. (seperti gambar berikut)
    ![Django Rocket](https://global.discourse-cdn.com/business7/uploads/djangoproject/original/3X/6/b/6b2c3c21ef8b9458b7eb6bdc843333e154b477d2.png)
13. Hentikan server dengan cara menekan `Ctrl+C` pada cmd.
14. Non aktifkan virtual environment (env) dengan command :
    ```bash
    deactivate
    ```

##### Check 2 : Membuat aplikasi dengan nama `main` pada proyek tersebut.

15. Buatlah aplikasi baru dengan nama **main** dengan menjalankan perintah berikut :
    ```bash
    python manage.py startapp main
    ```
16. Bukalan berkas `settings.py` di dalam direktori proyek `umkami`.
17. Tambahkanlah `'main'` ke dalam variabel `INSTALLED_APPS` seperti contoh berikut :
    ```python
    INSTALLED_APPS = [
        ...,
        'main'
    ]
    ```

##### Check 3 : Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`

18. Bukalah berkas `urls.py` di dalam direktori proyek `umkami`, **bukan yang ada di direktori `main`.**
19. Lakukan perubahan pada isi berkas tersebut seperti contoh kode berikut:

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```

##### Check 4 : Membuat model pada aplikasi `main` dengan nama Product dan memiliki atibut wajib.

20. Di direktori `main`, bukalah berkas `models.py`
21. Isilah berkas `models.py` dengan kode berikut :

    ```python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.IntegerField()
        description = models.TextField()

        def __str__(self):
            return self.name

    ```

22. Lakunlah migrasi model dengan menjalankan perintah berikut.
    ```bash
    python manage.py makemigrations
    ```
23. Terapkanlah migrasi ke dalam basis data lokal dengan menjalankan perintah berikut.
    ```bash
    python manage.py migrate
    ```

- Note: Setiap ada perubahan pada `models.py`, silahkan lakukan langkah 22 dan 23 kembali.

##### Check 5 : Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ html yang menampilkan nama aplikasi serta nama dan kelas kamu.

24. Bukalah berkas `views.py` yang terletak pada direktori `main`.
25. Gantilah isi berkas tersebut dengan kode berikut :

    ```python
    from django.shortcuts import render

    def home_view(request):
        context = {
            'app_name': 'UMKaMi',
            'student_name': 'Oscar Ryanda Putra',
            'student_class': 'PBP F',
        }
        return render(request, 'home.html', context)
    ```

26. Buatlah direktori baru bernama `templates` dalam direktori `main`.
27. Di dalam direktori `templates`, buatlah berkas baru dengan nama `home.html`. Isi berkas `home.html` dengan kode berikut :

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ app_name }}</title>
    </head>
    <body>
        <h1>{{ app_name }}</h1>
        <p>Nama: {{ student_name }}</p>
        <p>Kelas: {{ student_class }}</p>
    </body>
    </html>
    ```

##### Check 6 : Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

28. Buatlah berkas baru bernama `urls.py` di dalam direktori main.
29. Isi berkas tersebut dengan kode berikut :

    ```python
    from django.urls import path
    from .views import home_view

    urlpatterns = [
        path('', home_view, name='home'),
    ]
    ```

###### RUNNING DAN TESTING PROYEK

30. Jalankan proyek Django dengan perintah berikut.
    ```bash
    python manage.py runserver
    ```
31. Bukalah laman http://localhost:8000/ dan lihat perubahannya.


##### Check 7: Membuat _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-teman.

###### ADD, COMMIT, PUSH GITHUB :

32. Lakukan inisiasi direktori lokal `umkami` sebagai repositori git dengan menjalankan perintah berikut pada terminal :
    ```bash
    git init
    ```
33. Kemudian, tandai semua _file_ yang berada pada direktori tersebut sebagai _file_ yang akan di-_commit (tracked)_ dengan perintah berikut :
    ```bash
    git add .
    ```
34. Lanjutkan membuat pesan _commit_ yang sesuai dengan perubahan atau pembaharuan dengan perintah berikut :
    ```bash
    git commit -m "<PESAN KAMU>"
    ```
35. Pastikan saat ini kamu berada pada branch _main_ dengan menjalankan perntah berikut :
    ```bash
    git branch -M main
    ```
36. Hubungkan repositori lokal (direktori saat ini) dengan repositori di Github kamu dengan perintah berikut :
    ```bash
    git remote add origin <URL_REPO>
    ```

- Note : ubah `<URL_REPO>` dengan url github yang baru kamu buat.

37. Kemudian, push seluruh berkas ke repositori github dengan perintah berikut :
    ```bash
    git push -u origin main
    ```

###### PUSH PWS :

38. Buka halaman PWS pada https://pbp.cs.ui.ac.id/ , kemudian buatlah akun atau _Register_ menggunakan akun SSO kamu.
39. Lakukan _login_ menggunakan akun yang baru saja kamu buat.
40. Buatlah proyek baru dengan menekan tombol `Create New Project`. Kamu akan berpindah ke halaman untuk membuat proyek baru. Silahkan isi `Project Name` dengan umkami. Setelah itu, tekan tombol `Create New Project` yang berwarna biru.
41. Simpan informasi _Project Credentials_ di tempat yang dan pastikan tidak hilang karena akan digunakan di langkah selanjutnya. **Jangan jalankan dulu instruksi _Project Command_.**
42. Lakukanlah update pada berkas `settings.py` di proyek Django kamu, tambahkan URL _deployment PWS_ pada variabel `ALLOWED_HOSTS` seperti kode berikut :
    ```python
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", <NAMA DEPAN>-<NAMA TENGAH>-umkami.pbp.cs.ui.ac.id]
    ...
    ```

- Note : ganti `<NAMA DEPAN>` dan `<NAMA TENGAH>` sesuai akun SSO kamu. Misal : oscar-ryanda-umkami.pbp.cs.ui.ac.id .

43. Jalankan perintah berikut untuk melakukan push repositori lokal ke PWS kamu (jalankan satu per satu tiap baris) :

    ```bash
    git remote add pws http://pbp.cs.ui.ac.id/<USERNAME PWS>/umkami

    git branch -M master

    git push pws master
    ```

44. Setelah menjalankan perintah tersebut, kamu akan diminta `username` dan `password`. Gunakan _Project Credentials_ yang telah kamu simpan (ingat kembali langkah 45).
45. Setelah menjalankan perintah tersebut, silahkan kembalikan branch ke main dengan perintah berikut :
    ```bash
    git branch -M main
    ```
46. Cari proyek kamu di laman PWS, kemudian cek statusnya. Jika status `Building` maka tunggu beberapa saat hingga status berubah menjadi `Running`.
47. Jika sudah `Running`, silahkan tekan tombol `View Project` lalu copy linknya dan buka di aplikasi Google Chrome. Pastikan https:// diganti dengan http:// pada link tersebut.

### 2) Bagan _request client_ ke web pada Django

![Bagan request & response Django](https://media.discordapp.net/attachments/1144094248665370624/1282015001766395945/BAGAN_PBP.png?ex=66ddd103&is=66dc7f83&hm=c296e3f9ea94c7b1084bde785a88609e3748a6059ecaa520a224952b8eb231e0&=&format=webp&quality=lossless&width=825&height=463)

Bagan di atas menggambarkan siklus _request-response_ dalam aplikasi web Django. Berikut adalah penjelasan keterkaitan antara `urls.py`, `views.py`, `models.py`, dan berkas HTML dalam proses ini:

1.  **Client Request**: _Request_ dimulai dari klien (browser atau aplikasi lain dari pengguna) yang mengirimkan permintaan ke server.
2.  **urls.py**: Berkas ini berfungsi sebagai pengarah lalu lintas dalam aplikasi Django atau _routing_. Berkas ini yang menentukan URL mana yang perlu dipanggil dan view mana yang menanganinya. Ketika ada permintaan yang diterima, Django akan mencocokan URL dari permintaan dengan URL yang didefinisikan di `urls.py`.
3.  **views.py**: Setelah `urls.py` menentukan view mana yang harus merespons, kontrol dialihkan ke fungsi atau kelas di berkas `views.py`.
    View bertugas untuk memproses data yang diterima dan memberikan repsons yang sesuai kepada klien. Ini mungkin melibatkan pemanggilan data dari database melalui berkas model.
4.  **models.py**: View dapat berinteraksi dengan `models.py` untuk meminta data dari database.
    Berkas model pada Django mendefinisikan struktur data, menyediakan alat untuk manajemen database seperti mengambil, menambah atau mengubah data (query data).
5.  **Database**: berfungsi untuk menyimpan data yang nantinya akan diambil maupun ditambah.
6.  **models.py**: Data yang diambil dari database dikembalikan ke `models.py`, yang kemudian mengirimkannya kembali ke `views.py`.
7.  **views.py**: Setelah data diterima dari model, view memproses data tersebut dan mempersiapkan konten (biasanya berupa berkas HTML) untuk dikirim kembali ke klien.
8.  **HTML Template**: HTML templat diisi dengan data atau konteks yang disediakan oleh view. Templat ini kemudian di-render menjadi HTML lengkap yang siap dikirim ke klien melalui browser.
9.  **Client Response**: HTML yang sudah di-render dikirim kembali ke klien sebagai respons atas permintaan awal mereka.

### 3) Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git adalah alat penting dalam pengembangan perangkat lunak yang digunakan untuk melacak perubahan pada kode. Fungsinya sangat membantu, terutama kalau kita bekerja dalam tim atau mengerjakan proyek besar. Berikut beberapa fungsi utama Git yang bisa membantu:

1. Mencatat Semua Perubahan: Git menyimpan catatan tentang semua perubahan yang kita buat di dalam proyek. Jadi, kalau kita melakukan kesalahan atau ingin melihat versi kode sebelumnya, kita bisa "balik" ke versi yang lebih lama dengan mudah.

2. Kerja Tim Lebih Mudah: Dengan Git, banyak orang bisa bekerja di proyek yang sama tanpa takut saling menimpa kode. Setiap orang bisa bekerja di bagian mereka sendiri, lalu menggabungkannya nanti setelah selesai. Ini sangat berguna untuk kolaborasi tim.

3. Menyelesaikan Konflik Kode: Kalau dua orang mengubah file yang sama, Git akan mendeteksi adanya konflik. Kita bisa melihat perbedaan tersebut dan memutuskan perubahan mana yang ingin disimpan.

4. Menyimpan Proyek Secara Online: Git memungkinkan kita menyimpan proyek di repositori online seperti GitHub. Ini berguna untuk backup, dan kita bisa mengakses proyek kita dari mana saja, selama ada internet.

5. Membuat Cabang untuk Eksperimen: Git memungkinkan kita membuat branch (cabang) untuk mengerjakan fitur baru atau mencoba sesuatu tanpa merusak kode utama. Setelah semuanya siap, kita bisa menggabungkan cabang itu ke proyek utama.

6. Otomatisasi Pengujian dan Deployment: Git sering digunakan bersama alat lain untuk otomatisasi pengujian dan deployment aplikasi. Jadi, setiap kali kita mengubah kode dan mengunggahnya, pengujian bisa dilakukan secara otomatis sebelum aplikasi diperbarui.

Dengan Git, pengembangan perangkat lunak jadi lebih terorganisir dan kita bisa bekerja lebih aman. Meskipun terlihat agak rumit di awal, Git sangat berguna setelah kita memahaminya.


### 4) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, Django menjadi pilihan utama karena kita sebagai mahasiswa FASILKOM UI sudah mempelajari dasar bahasa Python di semester 1, yang merupakan bahasa yang digunakan oleh Django. Hal ini tentu memudahkan dan mempercepat proses pembelajaran Django tanpa perlu mempelajari ulang Python. Selain itu, Django memiliki struktur yang tertata rapi dengan menggunakan pola desain "Model-View-Template" (MVT), sehingga memudahkan pemula untuk memahami bagaimana aplikasi web berinteraksi dengan database, mengelola logika, dan menampilkan data. Django juga dilengkapi dengan library yang sangat lengkap, menawarkan banyak fitur bawaan seperti sistem autentikasi dan pengelolaan formulir, yang mengurangi kebutuhan untuk menulis kode dari awal.

Ada banyak keunggulan lain dari Django, tetapi poin-poin di atas sudah mencakup kelebihan utamanya.

### 5) Mengapa model pada Django disebut sebagai ORM?

Model dalam Django disebut ORM, yang merupakan singkatan dari "Object-Relational Mapping". ORM memungkinkan pengembang berinteraksi dengan database menggunakan kode berbasis objek, tanpa harus menulis SQL langsung.

Berikut adalah beberapa alasan mengapa model Django disebut ORM:

1. Abstraksi: Django ORM menyediakan lapisan abstraksi yang memudahkan pengembang untuk berinteraksi dengan database melalui objek Python, sehingga mereka lebih fokus bekerja dengan konsep Python daripada harus berurusan dengan detail SQL.
2. Manajemen Data: Dengan ORM, objek Python dapat dengan mudah dibuat, dibaca, diperbarui, dan dihapus di dalam database, tanpa perlu menulis kueri SQL secara langsung.
3. Portabilitas: Kode yang menggunakan ORM lebih mudah dipindahkan antar jenis database. Jadi, jika ingin mengganti jenis database, perubahan yang dibutuhkan hanya sedikit di konfigurasi.
4. Keamanan: ORM membantu meningkatkan keamanan aplikasi dengan mengurangi risiko injeksi SQL, karena kueri yang dibentuk melalui ORM lebih terstruktur dan lebih terkontrol.
5. Efisiensi Pengembangan: Penggunaan ORM mempercepat proses pengembangan karena mengurangi jumlah kode yang perlu ditulis dan diuji, serta menjaga kode tetap bersih dan mudah dipahami hanya dengan menggunakan satu bahasa.