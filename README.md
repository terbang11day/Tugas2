# **Toku-ku**

**Daftar isi :**<br/>
[Tugas 2](#tugas-2)<br/>
[Tugas 3](#tugas-3)<br/>
[Tugas 4](#tugas-4)<br/>

**Thariq Ziyad Al Farizi**<br/>
**2206082865**<br/>
**PBP B**<br/>

# **Tugas 2**
## **Langkah pengerjaan tugas 2 PBP**

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)?

   1. Buat proyek dan aplikasi dengan nama 'tugas2' dan tambahkan aplikasi dengan nama main
   2. kongigurasi routing agara aplikasi dapat diakses melaluii URL
   3. buat model item di dalam aplikasi dengan atribut nama,price,amount,stock dan description dengan tipe data yang     dibutuhkan
   4. render template html dengan membuat fungsi views.py
    5. routing untuk mengaitkan view dengan url
    6. deployment aplikasi dengan adaptable
    7. lengkapi berkas Readme.md

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan   tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/flowchart.jpg?raw=true)

    **Alur Kerja Django**

    ketika pengguna mengunjungi situs web Django, mereka mengirimkan permintaan ke server web. Server web kemudian meneruskan permintaan tersebut ke aplikasi Django.

    **Request dari Klien**

    klien mengirimkan permintaan dengan membuka alamat URL yang sesuai di browser. Alamat URL ini dapat berupa URL halaman web, URL untuk menjalankan fungsi tertentu, atau URL untuk mengakses data dari database.

    **urls.py**

    berkas `urls.py` di proyek Django digunakan untuk mengaitkan URL dengan view yang sesuai. View adalah fungsi Python yang bertanggung jawab untuk menangani permintaan dan merender halaman web.

    **views.py**

    view diakses sesuai dengan URL yang dikunjungi oleh klien. View berisi logika untuk mengolah permintaan dan menyiapkan data yang akan ditampilkan dalam template HTML.

    **models.py**

    model digunakan untuk mendefinisikan struktur dan skema database. Model diakses oleh view ketika memerlukan akses atau manipulasi data dalam database.

    **Berkas HTML (Template)**

    template HTML digunakan untuk merender halaman web. View mengirimkan data dari model ke template untuk ditampilkan dalam halaman.

    **Respons ke Klien**

    setelah view selesai mengolah permintaan dan merender template, respons HTML dikirimkan kembali ke klien.

    **Kaitan Antara Komponen**

    * `urls.py` mengarahkan permintaan klien ke view yang sesuai berdasarkan URL.
    * `views.py` berisi logika untuk memproses permintaan, termasuk mengakses model jika diperlukan, dan merender template.
    * `models.py` mendefinisikan struktur database yang mungkin digunakan oleh view untuk mengakses atau menyimpan data.
    * Template HTML menerima data dari view dan digunakan untuk merender halaman web yang akan dikirimkan sebagai respons ke klien.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Kita menggunakan virtual environment karena itu adalah tempat terpisah di komputer kita untuk menyimpan semua alat dan potongan kode yang kita butuhkan untuk membuat aplikasi. Ini seperti memiliki kantong khusus untuk setiap proyek agar tidak bercampur aduk. Tanpa virtual environment, kita bisa membuat aplikasi Django, tapi itu akan menjadi lebih sulit untuk mengelola dan bisa menyebabkan masalah. Jadi, lebih baik selalu gunakan virtual environment saat membuat aplikasi web dengan Django atau proyek Python lainnya agar semuanya teratur dan aman.


4. Perbedaan antara MVC, MVT, dan MVVM:

    * MVC (Model-View-Controller):
        adalah model yang bertanggung jawab terhadap interaksi pengguna, mengelola alur aplikasi
        dan memutuskan bagaimana data ditampilkan

    * MVT (Model-View-Template) :
        Adalah model yang bertanggung jawab terhadap pengelolaan permintaan dan merender template

    * MVVM (Model-View-ViewModel):
        Adalah model yang bertanggung jawab menampilkan data dan menrima input pengguna, seta menyediakan pemisah antara view dan model


** Note 

    * http://127.0.0.1:8000/main/ tautan menuju tampilan web
    * http://127.0.0.1:8000/admin/ tautan menuju databse
    * terdapat penambahan tescase yaitu apakah suatu data terdapat pada laman web tersebut
    * Visualisasi Database dalam bentuk tabel kepad client sehingga mudah dibaca
    * Pengelolaan database pada bentuk admin, web diakses dengan /admin pada bagian belakangnya



# **Tugas 3**


1. Apa perbedaan antara form POST dan form GET dalam Django?
    *Form GET:
        Data dari form terlihat di alamat URL.
        Digunakan untuk mengambil informasi dari server, seperti pencarian.

    *Form POST:
        Data dari form tidak terlihat di alamat URL.
        Digunakan untuk mengirim data pribadi atau melakukan perubahan di server, seperti mengirim pesan atau mengisi formulir.
    
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

    *XML (eXtensible Markup Language):
        Digunakan untuk menyimpan dan mentransfer data.
        Formatnya sangat struktural dengan tag yang mendefinisikan data.
        Lebih fleksibel tetapi lebih berat daripada JSON dan HTML.
        Umumnya digunakan dalam pertukaran data antar sistem.
        
    #JSON (JavaScript Object Notation):
        Digunakan untuk menyimpan dan mentransfer data.
        Formatnya ringkas dan mudah dibaca oleh manusia.
        Biasanya digunakan dalam pengembangan aplikasi web dan layanan web (API).
        
    *HTML (HyperText Markup Language):
        Digunakan untuk membuat tampilan halaman web dan struktur konten.
        Berfokus pada representasi visual dan interaktivitas di dalam browser web.
        Tidak digunakan untuk pengiriman data, melainkan untuk menampilkan konten dan mengatur tampilan halaman web.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

    *Formatnya ringkas dan mudah dibaca oleh manusia.
    *Mendukung struktur data yang fleksibel dan kompleks, seperti objek dan larik bersarang.
    *Kompatibel dengan bahasa pemrograman yang umum digunakan, sehingga mudah diolah oleh aplikasi.
    *Cocok untuk pengembangan aplikasi web dan layanan web (API) karena memudahkan pertukaran data antara klien dan server.
    *Dukungan browser web terintegrasi untuk parsing JSON memudahkan komunikasi asinkron antara browser dan server.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

    Hal-hal yang saya lakukan untuk menyelesaikan tugas ini adalah :

    *Buat file forms.py untuk membuat form input data baru (ItemForm).
    *Buat file HTML create_product.html untuk menampilkan form input data.
    *Buat fungsi create_product di views.py untuk menampilkan form, memvalidasi input, dan menyimpan data.
    *Tambahkan tombol di home.html untuk menuju halaman pengisian form dan tampilkan jumlah item dan total amount di sana.
    *Konfigurasi URL di urls.py untuk mengarahkan URL 'create_product/' ke fungsi create_product di views.py.
    *Buat fungsi show_xml dan show_json di views.py untuk menghasilkan file XML dan JSON dari data Item.
    *Tambahkan URL 'xml/' dan 'json/' di urls.py untuk menampilkan file XML dan JSON.
    *Buat fungsi show_xml_by_id dan show_json_by_id di views.py untuk menampilkan XML dan JSON berdasarkan ID.
    *Tambahkan URL 'xml/int:id/' dan 'json/int:id/' di urls.py untuk menampilkan XML dan JSON berdasarkan ID yang diminta.

5.  SS Postman
   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/html.png)?raw=true)
<<<<<<< HEAD

=======
>>>>>>> abfe070930663428f1c0ae3fc77b3a404c8fe9e3
   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/json.png?raw=true)

   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/json_id.png)?raw=true)

   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/xml.png?raw=true)
   
   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/xml_id.png?raw=true)


# **Tugas 4**

1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

    Django UserCreationForm adalah salah satu formulir bawaan yang disediakan oleh Django untuk mengelola proses pendaftaran pengguna (user registration). Formulir ini memudahkan pengembang web untuk membuat halaman pendaftaran dengan fitur validasi dan penyimpanan data pengguna ke dalam database. Kelebihan dari menggunakan UserCreationForm adalah kemudahan penggunaannya dan integrasi yang baik dengan sistem otentikasi Django. Namun, kekurangannya adalah kurangnya kustomisasi yang dapat dilakukan secara langsung, sehingga mungkin memerlukan penyesuaian tambahan jika Anda memiliki kebutuhan yang sangat khusus.

2. Apa perbedaan antara `autentikasi` dan `otorisasi` dalam konteks Django, dan mengapa keduanya penting?

    ```Autentikasi```: Autentikasi adalah proses verifikasi identitas pengguna. Dalam konteks Django, ini berarti memastikan bahwa seseorang yang mencoba mengakses aplikasi web Anda adalah pengguna yang sah dan telah terautentikasi (misalnya, dengan username dan password). Django menyediakan sistem otentikasi bawaan yang dapat mengelola autentikasi pengguna dengan aman.

    ```Otorisasi``` Otorisasi adalah proses yang menentukan apa yang dapat dilakukan oleh pengguna yang telah terautentikasi. Ini adalah langkah selanjutnya setelah autentikasi. Django memiliki sistem otorisasi yang memungkinkan Anda untuk mengatur izin akses pengguna ke berbagai bagian aplikasi Anda. Misalnya, seorang pengguna yang terautentikasi mungkin memiliki izin untuk mengedit profilnya sendiri, tetapi tidak memiliki izin untuk mengedit profil pengguna lain.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

    Cookies adalah kecil berkas data yang disimpan di sisi klien (browser) yang digunakan untuk menyimpan informasi sesi atau preferensi pengguna. Dalam aplikasi web, cookies dapat digunakan untuk mengelola sesi pengguna, seperti menyimpan ID sesi atau mengingat preferensi pengguna.

    Django menggunakan cookies untuk mengelola sesi pengguna. Secara default, Django menyimpan ID sesi pengguna dalam cookie. Ini memungkinkan Django untuk mengidentifikasi pengguna yang telah terautentikasi dan menjaga status sesi mereka.

    Penggunaan cookies dalam pengembangan web dapat menjadi aman jika diimplementasikan dengan benar. Namun, ada beberapa risiko potensial yang harus diwaspadai:



4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

    `Cross-Site Scripting (XSS)` Penyerang dapat mencoba menyisipkan skrip berbahaya ke dalam cookie, yang akan dieksekusi oleh browser pengguna.

    `Cross-Site Request Forgery (CSRF)`Serangan CSRF dapat memanipulasi tindakan yang diambil oleh pengguna yang telah terotentikasi dalam aplikasi web dengan menggunakan cookie mereka.

    `Penyadapa` Cookies bisa dicuri jika tidak dienkripsi dengan baik atau jika ada celah keamanan dalam aplikasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    *Buat model Item dan User dalam aplikasi Anda. Pastikan Anda menentukan relasi antara keduanya, misalnya dengan menggunakan ForeignKey untuk menghubungkan setiap item dengan pengguna yang membuatnya.

    *Buat migrasi untuk model Anda dengan perintah python manage.py makemigrations dan terapkan migrasi tersebut dengan python manage.py migrate.

    *Buat skrip manajemen khusus untuk membuat tiga dummy data untuk masing-masing akun pengguna. Anda dapat menggunakan User.objects.create_user untuk membuat pengguna dan Item.objects.create untuk membuat item terkait.












