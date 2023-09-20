1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)?

    * Buat proyek dan aplikasi dengan nama "tugas2" dan tambahkan aplikasi dengan nama main
    * kongigurasi routing agara aplikasi dapat diakses melaluii URL
    * buat model item di dalam aplikasi dengan atribut nama,price,amount,stock dan description dengan tipe data yang     dibutuhkan
    * render template html dengan membuat fungsi views.py
    * routing untuk mengaitkan view dengan url
    * deployment aplikasi dengan adaptable
    * lengkapi berkas Readme.md

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan   tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

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


TUGAS 2 

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
    *Untuk bonus, gunakan Item.objects.count() untuk menghitung jumlah item dan Item.objects.all() untuk mendapatkan semua item dan menghitung total amount.
    *Tambahkan tombol di home.html untuk menuju halaman pengisian form dan tampilkan jumlah item dan total amount di sana.
    *Konfigurasi URL di urls.py untuk mengarahkan URL 'create_product/' ke fungsi create_product di views.py.
    *Buat fungsi show_xml dan show_json di views.py untuk menghasilkan file XML dan JSON dari data Item.
    *Tambahkan URL 'xml/' dan 'json/' di urls.py untuk menampilkan file XML dan JSON.
    *Buat fungsi show_xml_by_id dan show_json_by_id di views.py untuk menampilkan XML dan JSON berdasarkan ID.
    *Tambahkan URL 'xml/int:id/' dan 'json/int:id/' di urls.py untuk menampilkan XML dan JSON berdasarkan ID yang diminta.

5. ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/html.png?raw=true)
   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/json.png?raw=true)
   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/json_1.png?raw=true)
   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/xml.png?raw=true)
   ![alt text](https://github.com/terbang11day/Tugas2/blob/main/dok/xml_1.png?raw=true)







