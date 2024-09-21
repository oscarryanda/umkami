# Toko Ungu !

**_Disusun oleh : Jeremia Rangga Setyawan | 2306245775 | PBP B_**

**_Link PWS : http://jeremia-rangga-tokoungu.pbp.cs.ui.ac.id_**

## Tugas 2

### 1) Proses Pembuatan Projek Django

##### Check 1 : Membuat sebuah proyek Django baru

1. Buatlah sebuah direktory baru bernama `toko-ungu` di komputer

2. Kemudian, buat juga _repository_ baru di Github bernama sama yaitu `toko-ungu` dengan visibility _public_.

3. Dalam direktory baru tersebut, buka _command prompt_

4. Buatlah _virtual enviroment_ menggunakan python dengan command :

```bash

python -m venv env

```

5. Lalu, aktifkan _virtual environement_ dengan command :

```bash

env\Scripts\activate

```

6.  _Virtual environment_ akan aktif yang ditandai (env) di awal baris input terminal

7.  Buatlah file dengan nama `requirements.txt` di dalam direktori yang sama dan tambahkan beberapa _dependencies_ berikut di file tersebut :

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

9. Buatlah proyek Django baru dengan nama `toko_ungu` dengan command :

```bash

django-admin startproject toko_ungu .

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

16. Bukalan berkas `settings.py` di dalam direktori proyek `toko_ungu`.

17. Tambahkanlah `'main'` ke dalam variabel `INSTALLED_APPS` seperti contoh berikut :

```python

INSTALLED_APPS = [

...,

'main'

]

```

##### Check 3 : Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`

18. Bukalah berkas `urls.py` di dalam direktori proyek `toko_ungu`, **bukan yang ada di direktori `main`.**

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



class  Product(models.Model):

name = models.CharField(max_length=255)

description = models.TextField()

price = models.IntegerField()

quantity = models.IntegerField()



@property

def  is_available(self):

return  self.quantity > 0

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



def  show_main(request):

context = {

'app' : 'Toko Ungu',

'name': 'Jeremia Rangga',

'class': 'PBP B'

}



return render(request, "main.html", context)

```

26. Buatlah direktori baru bernama `templates` dalam direktori `main`.

27. Di dalam direktori `templates`, buatlah berkas baru dengan nama `main.html`. Isi berkas `main.html` dengan kode berikut :

```html
<h1>{{ app }}</h1>

<h5>Name:</h5>

<p>{{ name }}</p>

<p></p>

<h5>Class:</h5>

<p>{{ class }}</p>

<p></p>
```

##### Check 6 : Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

28. Buatlah berkas baru bernama `urls.py` di dalam direktori main.

29. Isi berkas tersebut dengan kode berikut :

```python

from django.urls import path

from main.views import show_main



app_name = 'main'



urlpatterns = [

path('', show_main, name='show_main'),

]

```

###### RUNNING DAN TESTING PROYEK

30. Jalankan proyek Django dengan perintah berikut.

```bash

python manage.py runserver

```

31. Bukalah laman http://localhost:8000/ dan lihat perubahannya.

32. Di direktori `main`, bukalah berkas `tests.py`.

33. Isi berkas tersebut dengan kode berikut :

```python

from django.test import TestCase, Client

from .models import Product



class  mainTest(TestCase):

def  test_main_url_is_exist(self):

response = Client().get('')

self.assertEqual(response.status_code, 200)



def  test_main_using_main_template(self):

response = Client().get('')

self.assertTemplateUsed(response, 'main.html')



def  test_nonexistent_page(self):

response = Client().get('/skibidi/')

self.assertEqual(response.status_code, 404)



def  test_available(self):

product = Product.objects.create(

name="Baju",

description="Warna putih",

price = 100000,

quantity = 10,

)

self.assertTrue(product.is_available)

```

34. Jalankanlah berkas tes menggunakan perintah berikut :

```bash

python manage.py test

```

35. Jika tes berhasil dan aman, maka akan muncul informasi berikut :

```bash

Found 4 test(s).

Creating test database for alias 'default'...

System check identified no issues (0  silenced).

..

----------------------------------------------------------------------

Ran 4 tests in 0.016s



OK

Destroying test database for alias 'default'...

```

##### Check 7: Membuat _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-teman.

###### ADD, COMMIT, PUSH GITHUB :

36. Lakukan inisiasi direktori lokal `toko-ungu` sebagai repositori git dengan menjalankan perintah berikut pada terminal :

```bash

git init

```

37. Kemudian, tandai semua _file_ yang berada pada direktori tersebut sebagai _file_ yang akan di-_commit (tracked)_ dengan perintah berikut :

```bash

git add .

```

38. Lanjutkan membuat pesan _commit_ yang sesuai dengan perubahan atau pembaharuan dengan perintah berikut :

```bash

git commit -m "<PESAN KAMU>"

```

39. Pastikan saat ini kamu berada pada branch _main_ dengan menjalankan perntah berikut :

```bash

git branch -M main

```

40. Hubungkan repositori lokal (direktori saat ini) dengan repositori di Github kamu dengan perintah berikut :

```bash

git remote add origin <URL_REPO>

```

- Note : ubah `<URL_REPO>` dengan url github yang baru kamu buat.

41. Kemudian, push seluruh berkas ke repositori github dengan perintah berikut :

```bash

git push -u origin main

```

###### PUSH PWS :

42. Buka halaman PWS pada https://pbp.cs.ui.ac.id/ , kemudian buatlah akun atau _Register_ menggunakan akun SSO kamu.

43. Lakukan _login_ menggunakan akun yang baru saja kamu buat.

44. Buatlah proyek baru dengan menekan tombol `Create New Project`. Kamu akan berpindah ke halaman untuk membuat proyek baru. Silahkan isi `Project Name` dengan tokoungu. Setelah itu, tekan tombol `Create New Project` yang berwarna biru.

45. Simpan informasi _Project Credentials_ di tempat yang dan pastikan tidak hilang karena akan digunakan di langkah selanjutnya. **Jangan jalankan dulu instruksi _Project Command_.**

46. Lakukanlah update pada berkas `settings.py` di proyek Django kamu, tambahkan URL _deployment PWS_ pada variabel `ALLOWED_HOSTS` seperti kode berikut :

```python

...

ALLOWED_HOSTS = ["localhost", "127.0.0.1", <NAMA DEPAN>-<NAMA TENGAH>-tokoungu.pbp.cs.ui.ac.id]

...

```

- Note : ganti `<NAMA DEPAN>` dan `<NAMA TENGAH>` sesuai akun SSO kamu. Misal : jeremia-rangga-tokoungu.pbp.cs.ui.ac.id .

47. Jalankan perintah berikut untuk melakukan push repositori lokal ke PWS kamu (jalankan satu per satu tiap baris) :

```bash

git remote add pws http://pbp.cs.ui.ac.id/<USERNAME PWS>/tokoungu



git branch -M master



git push pws master

```

48. Setelah menjalankan perintah tersebut, kamu akan diminta `username` dan `password`. Gunakan _Project Credentials_ yang telah kamu simpan (ingat kembali langkah 45).

49. Setelah menjalankan perintah tersebut, silahkan kembalikan branch ke main dengan perintah berikut :

```bash

git branch -M main

```

50. Cari proyek kamu di laman PWS, kemudian cek statusnya. Jika status `Building` maka tunggu beberapa saat hingga status berubah menjadi `Running`.

51. Jika sudah `Running`, silahkan tekan tombol `View Project` lalu copy linknya dan buka di aplikasi Google Chrome. Pastikan https:// diganti dengan http:// pada link tersebut.

### 2) Bagan _request client_ ke web pada Django

![Bagan Request dan Response](https://github.com/user-attachments/assets/f69c567f-7ddd-4e64-a591-8fc732006c4d)

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

GIT adalah alat yang digunakan oleh developer dan programmer sebagai sistem kontrol dalam pengembangan perangkat lunak. Tujuan utama dari GIT adalah untuk mengatur versi dari kode sumber, memungkinkan penentuan baris dan kode yang perlu ditambahkan atau diubah. Git dikembangkan oleh Linus Torvalds pada tahun 2005.

Berikut adalah fungsi git dalam pengembagan perangkat lunak :

1.  **Kontrol Versi**: Git memungkinkan _developer_ untuk menyimpan versi berbeda dari sebuah proyek (versi lama atau versi terkini). Hal ini memudahkan _developer_ untuk kembali ke versi sebelumnya, jika _software_ atau aplikasi mengalami masalah pada versi terbaru.

2.  **Kolaborasi**: Git sangat memudahkan kerja tim antar _developer_. Beberapa _developer_ dapat bekerja secara bersamaan pada proyek yang sama tanpa mengganggu pekerjaan orang lain. Git dapat mengelola perubahan dari semua _developer_ dan membantu menggabungkan atau _merging_ pekerjaan mereka secara efisien.

3.  **Pelacakan Perubahan**: Git mencatat setiap perubahan yang dibuat pada kode sumber atau kode utama. Ini mencakup informasi tentang siapa yang membuat perubahan, kapan perubahan itu dibuat, dan detail tentang apa yang diubah.

4.  **Pengembangan Paralel**: Git mendukung pembuatan cabang (_branches_) yang memungkinkan pengembang untuk bekerja pada fitur atau perbaikan secara terpisah dari kode utama (_main branch_). Cabang-cabang ini kemudian dapat digabungkan (_merge_) kembali ke cabang utama setelah pekerjaan selesai. Hal ini memudahkan _developer_ jika ingin mengembangkan fitur baru tanpa mengubah kode sumber atau kode utama.

5.  **Pemulihan**: Tersimpannya semua versi kode, memudahkan _developer_ untuk mengakses dan mengembalikan kode ke keadaan semula jika terjadi kesalahan atau data hilang.

6.  **Kemudahan Penggunaan**: Meskipun menyediakan fungsi kontrol versi yang canggih, Git dirancang untuk mudah digunakan. Ini memungkinkan _developer_ untuk fokus pada pengembangan perangkat lunak daripada mengelola perubahan kode.

7.  **Integrasi dengan Alat Lain**: Git dapat berintegrasi dengan baik dengan berbagai alat pengembangan perangkat lunak lainnya, termasuk _platform_ hosting seperti GitHub, GitLab, dan Bitbucket, serta alat pelacakan isu.

8.  **Kinerja Tinggi**: Git dirancang untuk memberikan kinerja yang cepat dan efisien bahkan dalam proyek dengan riwayat yang sangat besar atau bahkan banyak cabang (_branch_).

Pada intinya, git sangat berguna untuk pengembangan perangkat lunak. _Developer_ memungkinkan melakukan banyak hal seperti kolaborasi hingga penyimpanan perubahan kode dengan sangat mudah.

### 4) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, Django menjadi pilihan pertama karena kita sebagai mahasiswa FASILKOM UI sudah mempelajari dasar bahasa yang digunakan Django yaitu python di semester 1. Hal ini tentu mempermudah dan mempercepat pembelajaran framework Django tanpa perlu mempelajari lagi python. Selain itu, Django juga memiliki struktur yang terorganisir berdasarkan pola desain "Model-View-Template" (MVT), yang memudahkan pemula memahami bagaimana aplikasi web dapat berinteraksi dengan database, mengelola logika, dan menampilkan data. Django juga menawarkan library yang sangat lengkap, mencakup banyak fitur bawaan seperti sistem autentikasi dan formulir, yang mengurangi kebutuhan untuk menulis kode dari nol.

Tentu masih banyak lagi keunggulan dari Django. Namun, hal yang sudah saya sebutkan diatas mencakup keseluruhan keunggulan utama dari Django.

### 5) Mengapa model pada Django disebut sebagai ORM?

Model dalam Django disebut sebagai ORM, yang merupakan singkatan dari "Object-Relational Mapping". ORM memungkinkan _developer_ untuk berinteraksi dengan database menggunakan kode yang berorientasi objek, bukan dengan menggunakan SQL langsung.

Berikut adalah beberapa alasan mengapa model Django disebut sebagai ORM:

1.  **Abstraksi**: ORM di Django menyediakan lapisan abstraksi yang memungkinkan _developer_ untuk berinteraksi dengan database melalui objek Python. Ini mengabstraksi kompleksitas SQL, sehingga _developer_ dapat bekerja lebih banyak dengan konsep Python daripada dengan detail database.

2.  **Manajemen Data**: Dengan ORM, objek dalam kode Python dapat dengan mudah dibuat, dibaca, diperbarui, dan dihapus melalui database tanpa perlu menulis kueri SQL secara eksplisit.

3.  **Portabilitas**: Kode yang menggunakan ORM lebih portabel. Artinya, aplikasi Django dapat beralih antar jenis database dengan perubahan konfigurasi minimal.

4.  **Keamanan**: ORM juga membantu dalam meningkatkan keamanan aplikasi. Penggunaan ORM mengurangi risiko serangan injeksi SQL, karena kueri yang dibangun melalui ORM lebih terstruktur dan dikontrol ketat oleh sistem.

5.  **Efisiensi Pengembangan**: Menggunakan ORM mempercepat proses pengembangan karena mengurangi jumlah kode yang perlu ditulis dan diuji. Ini juga membantu dalam memelihara kode yang lebih bersih dan lebih mudah untuk dimengerti dengan menggunakan hanya satu bahasa.

## Tugas 3

### 1) Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery atau pengiriman data adalah aspek penting dalam implementasi platform karena berperan besar dalam memastikan kinerja, skalabilitas, dan keamanan platform. Berikut adalah beberapa alasan mengapa pengiriman data sangat diperlukan:

1. **Aksesibilitas**: Menjamin ketersediaan data yang diperlukan untuk pengguna dan sistem (tidak hanya terbatas dalam waktu ataupun tempat tertentu saja).
2. **Integrasi**: Menyediakan kemampuan pertukaran data dengan sistem lain untuk keperluan integrasi antar platform atau aplikasi.
3. **Performa**: Mampu mempertahankan kecepatan dan skalabilitas platform melalui pengiriman data dengan volume yang besar secara efesien.
4. **Keamanan**: Memastikan data aman selama transit dan menghindari akses tidak sah dalam proses pengiriman data.
5. **Pengalaman Pengguna**: Meningkatkan responsivitas dan kepuasan pengguna melalui pengiriman data yang cepat.

### 2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya sendiri, JSON lebih baik dibandingkan dengan XML karena JSON terbilang lebih mudah untuk dibaca oleh manusia (berbentuk seperti dictionary dalam python) dan memiliki kemampuan pengiriman data yang lebih cepat. Selain itu, JSON memiliki kemampuan untuk menyimpan _array_, sedangkan XML tidak memiliki kemampuan tersebut. Walaupun memang XML memiliki sintaks yang mirip dengan HTML, namun secara _readability_ cukup sulit bagi kita manusia. Pada intinya, XML dan JSON memiliki fungsi yang sama yaitu untuk pengiriman data namun memiliki bentuk sintaks dan kemampuan yang berbeda.

JSON lebih populer dibandingkan XML karena sekali lagi memiliki sintaks atau format yang lebih mudah untuk dibaca oleh mansuia. Selain itu, JSON juga memiliki baris kode yang jauh lebih sedikit dibandingkan XML sehingga membuat JSON memiliki kemampuan pengiriman data yang lebih cepat.

### 3) Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?

Sesuai namanya, method `is_valid()` berfungsi untuk mengecek apakah data yang telah dimasukkan ke dalam form sudah memenuhi kriteria validasi yang telah ditentukan di form fields (entah itu CharField, IntegerField, TextField atau lainnya) kemudian me-_return_ _boolean_. Selain itu, method tersebut juga berfungsi untuk mengonversi inputan ke tipe python yang sesuai, memastikan tidak ada karakter yang ilegal dan mengatur data sesuai format yang diperlukan.

Kita membutuhkan method tersebut untuk keamanan data dengan memvalidasi kembali data sebelum dikirimkan ke database agar mengurangi adanya data berbahaya yang berpotensi menyebabkan error pada sisi server. Selain itu, pengguna atapun pengembang juga akan mendapatkan _feedback_ yang jelas mengenai kesalahan atau error yang terjadi pada input form data melalui method tersebut.

### 4) Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Token CSRF (Cross-Site Request Forgery) adalah komponen keamanan penting yang digunakan dalam pengembangan web untuk melindungi situs web dari serangan CSRF. Ini sangat penting dalam platform seperti Django yang secara otomatis menangani banyak aspek keamanan, termasuk perlindungan CSRF.

Berikut adalah beberapa fungsi dari token CSRF :

1. Verifikasi _request client_
   Token ini melakukan pengecekan bahwa permintaan atau request yang diterima oleh server berasal dari pengguna atau situs yang benar dan sah. Setiap sesi pengguna memiliki token unik ini dan ditambahkan dalam form sebagai hidden field yang harus dikirimkan kembali ke server setiap melakukan submission form.
2. Pencegahan Serangan CSRF
   Dengan melakukan verifikasi terhadap token CSRF, maka Django dapat memastikan dan menolak permintaan form yang tidak memiliki atau memiliki token yang tidak valid untuk mencegah serangan dari pengguna atau situs yang tidak sah.

Jika kita tidak menggunakan token CSRF, maka penyerang dapat melakukan permintaan berbahaya (seperti POST) yang dapat dilakukan oleh browser pengguna tanpa sepengetahuan atau persetujuan dari pengguna tersebut. Hal ini bisa membuat penyerang melakukan perubahan kata sandi, melakukan transaksi atau mengubah pengaturan akun tanpa sepengetahuan pengguna.

Penyerang dapat memanfaatkan ketidakhadiran CSRF token dengan mengirimkan form palsu. Penyerang dapat membuat laman web yang ketika dikunjungi oleh pengguna, secara otomatis mengirimkan form ke aplikasi Django tanpa sepengetahuan pengguna tersebut. Selain itu, penyerang juga bisa memanfaatkan _img tag_ atau javascript untuk membuat permintaan yang keliru dan tidak dapat dibedakan oleh Django.

### 5) Implementasi chekclist form

##### Check 1 : Membuat input `form` untuk menambahkan objek model pada app sebelumnya.

1. Membuat berkas `forms.py` pada direktori `main` dengan berisi kode berikut :

```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
```

2. Sebelum melanjutkan, saya perlu mengimplementasikan _skeleton_ sebagai kerangka views. Saya membuat direktori baru bernama `templates` pada direktori utama dan membuat berkas baru bernama `base.html` dengan isi kode berikut :

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1"
    />
    <title>Toko Ungu</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
    {% block meta %} {% endblock meta %}
  </head>
  <body>
    <!-- Navbar -->
    <nav
      class="navbar"
      data-bs-theme="dark"
      style="background-color: #742bcf"
    >
      <div class="container-fluid">
        <a
          class="navbar-brand"
          href="#"
          ><b>Toko Ungu</b></a
        >
      </div>
    </nav>
    <!-- END Navbar -->
    {% block content %} {% endblock content %}

    <!-- Bootstrap Script -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
    <!-- END Bootstrap Script -->
  </body>
</html>
```

- Saya menggunakan library bootstrap untuk mempercantik tampilan website.

3. Menambahkan kode berikut pada berkas `settings.py` di direktori proyek `toko_ungu` :

```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]
...
```

4. Mengubah kode pada berkas `main/templates/main.html` yang telah dibuat pada tugas sebelumnya menjadi sebagai berikut :

```html
{% extends 'base.html' %} {% block content %}

<!-- Name Card -->
<div class="p-3">
  <div class="card">
    <div class="card-header">
      <b><em>{{app}}</em></b> made with ❤️ By :
    </div>
    <div class="card-body">
      <blockquote class="blockquote mb-0">
        <p>{{ name }}</p>
        <footer class="blockquote-footer">{{ class }} | 2306245775</footer>
      </blockquote>
    </div>
  </div>
</div>
<!-- END Name Card -->
{% endblock content %}
```

5. Saya juga perlu menambahkan field baru yaitu id sebagai pengamanan pada `/main/models.py` sebagai berikut :

```python
from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    @property
    def is_available(self):
        return self.quantity > 0
```

6. Jangan lupa untuk melakukan migrasi dengan perintah sebagai berikut :

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Membuat method baru bernama `create_product` di berkas `/main/views.py` yang berfungsi untuk menambah entri produk baru ke database dan menambahkan beberapa baris kode pada berkas tersebut. Berikut kodenya :

```python
from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Product.objects.all()

    context = {
        'app' : 'Toko Ungu',
        'name': 'Jeremia Rangga',
        'class': 'PBP B',
        'products': products,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST" :
        form.save()
        return redirect('main:show_main')

    context = {'form': form}

    return render(request, "create_product.html", context)
```

8. Mengimplementasikan form yang baru saja dibuat ke dalam berkas laman baru bernama `/templates/create_product.html` dengan menggunakan `base.html`. Berikut kodenya :

```html
{% extends 'base.html' %} {% block content %}

<!-- Card -->
<div class="p-3">
  <div class="card">
    <div class="card-header"><b>Add New Product :</b></div>
    <div class="card-body">
      <form method="POST">
        {% csrf_token %}
        <table>
          {{ form.as_table }}
          <tr>
            <td></td>
            <td>
              <input
                type="submit"
                value="Add Product"
              />
            </td>
          </tr>
        </table>
      </form>
    </div>
  </div>
</div>
<!-- END Card -->

{% endblock %}
```

9. Melakukan routing URL laman tersebut di file `/main/urls.py`. Berikut kodenya :

```python
urlpatterns = [
    ...
    path('create-product', create_product, name='create_product'),
    ...
]
```

10. Menampilkan database produk yang telah terdaftar ke laman utama `main.html`. Berikut penambahan kodenya :

```html
...
<!-- Product Card -->
<div class="p-3">
  <div class="card">
    <div class="card-header">Registered Product :</div>
    <div class="card-body">
      {% if not products %}
      <p>Belum ada product pada Toko Ungu.</p>
      {% else %}
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Product Name</th>
            <th scope="col">Description</th>
            <th scope="col">Price</th>
            <th scope="col">Quantity</th>
          </tr>
        </thead>

        <tbody>
          {% for p in products %}
          <tr>
            <td>{{p.name}}</td>
            <td>{{p.description}}</td>
            <td>{{p.price}}</td>
            <td>{{p.quantity}}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
      {% endif %}

      <br />

      <a href="{% url 'main:create_product' %}">
        <button>Add New Product</button>
      </a>
    </div>
  </div>
</div>
<!-- END Product Card -->
{% endblock %}
```

##### Check 2 : Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML _by ID_, dan JSON _by ID_.

11. Membuat beberapa fungsi baru untuk menampilkan JSON dan XML baik secara keselurhan ataupaun per entri database pada berkas `/main/views.py`. Berikut kodenya :

```python
...
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
...
```

##### Check 3 : Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada Check 2.

12. Melakukan routing kembali URL funsgi tersebut pada file `/main/urls.py` dengan menambahkan kode berikut :

```python
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

13. Mencoba untuk menjalankan proyek dengan perintah `python manage.py runserver` dan membuka beberapa link yaitu http://localhost:8000/ untuk memastikan laman utama masih aman. Kemudian, link http://localhost:8000/xml/[id]/ atau http://localhost:8000/json/[id]/ untuk menampilkan data dalam bentuk xml ataupun json.

### 6) Screenshot Postman

1. JSON
   ![SS POSTMAN JSON](https://github.com/user-attachments/assets/76c310a0-9026-4b94-974a-ae8384e79166)

2. JSON By ID
   ![SS POSTMAN JSON By ID](https://github.com/user-attachments/assets/36a424d7-e490-4fec-b1f1-6a006b70667b)


4. XML
   ![SS POSTMAN XML](https://github.com/user-attachments/assets/6af8f540-1ec5-4e83-a041-bbabcae20725)


6. XML By ID
   ![SS POSTMAN XML By ID](https://github.com/user-attachments/assets/ea8ee1ed-bd56-49a4-9bd3-6b4051d10065)


Sekian & Terima Kasih
