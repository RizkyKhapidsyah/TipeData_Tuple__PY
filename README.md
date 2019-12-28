# TipeData_Tuple__PY

Bahan Ajar Fundamental Pemrograman Python. Mengenal Tipe Data Tuple dan List. Beserta Cara Melihat Perbedaannya.<br><br>
<img src="https://github.com/RizkyKhapidsyah/TipeData_Tuple__PY/blob/master/results/001.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/TipeData_Tuple__PY/blob/master/results/002.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/TipeData_Tuple__PY/blob/master/results/003.PNG"><br><br>

## Lihat Source Code :<br> 

> <a href="https://github.com/RizkyKhapidsyah/TipeData_Tuple__PY/blob/master/TipeData_Tuple__PY.py">Source Code: Contoh 1</a><br>
> <a href="https://github.com/RizkyKhapidsyah/TipeData_Tuple__PY/blob/master/TestTuple.py">Source Code: Contoh 2</a><br>
> <a href="https://github.com/RizkyKhapidsyah/TipeData_Tuple__PY/blob/master/TestTuple_2.py">Source Code: Contoh 3</a><br>

<br>

# Tipe Data Tuple Python

Sebuah tuple adalah urutan objek Python yang tidak berubah. Tuple adalah urutan, seperti daftar. Perbedaan utama antara tuple dan daftarnya adalah bahwa tuple tidak dapat diubah tidak seperti List Python. Tuple menggunakan tanda kurung, sedangkan List Python menggunakan tanda kurung siku.

Membuat tuple semudah memasukkan nilai-nilai yang dipisahkan koma. Secara opsional, Anda dapat memasukkan nilai-nilai yang dipisahkan koma ini di antara tanda kurung juga. Sebagai contoh :

      tup1 = ('fisika', 'kimia', 1993, 2017)
      tup2 = (1, 2, 3, 4, 5 )
      tup3 = "a", "b", "c", "d"

Tuple kosong ditulis sebagai dua tanda kurung yang tidak berisi apa-apa, contohnya : tup1 = (); Untuk menulis tupel yang berisi satu nilai, Anda harus memasukkan koma, meskipun hanya ada satu nilai, contohnya : tup1 = (50,) Seperti indeks String, indeks tuple mulai dari 0, dan mereka dapat diiris, digabungkan, dan seterusnya

Tipe data Tuple sangat mirip seperti tipe data List yang sudah kita pelajari sebelumnya, dimana tipe data Tuple juga terdiri dari kumpulan tipe data lain. Bedanya, anggota di dalam tipe data Tuple tidak bisa diubah setelah di deklarasikan. Kita akan bahas perbedaan ini menggunakan contoh kode program.

## Cara Pembuatan Tipe Data Tuple Python

Untuk membuat tipe data Tuple, gunakan tanda kurung biasa, kemudian setiap anggota list dipisah dengan tanda koma. Berikut contohnya:

      foo = ("Belajar", "Python", "di", "rikymetalist.blogspot.com")
      bar = (100, 200, 300, 400)
      baz = ("Python", 200, 6.99, True)
  
      print(foo)
      print(bar)
      print(baz)

Hasil kode program python:

<table>
  <thead>
    <tr>
      <th> 
      ('Belajar', 'Python', 'di', 'rikymetalist.blogspot.com')<br>
      (100, 200, 300, 400)<br>
      ('Python', 200, 6.99, True)
      </th>
    </tr>
  </thead>
</table>


Nyaris tidak berbeda dengan List. Namun tipe data Tuple dibuat menggunakan tanda kurung bulat, bukan tanda kurung siku sebagaimana List. Berikut pembuktiannya:

      foo = ["Belajar", "Python", "di", "rikymetalist.blogspot.com"]
      print(type(foo))
      foo = ("Belajar", "Python", "di", "rikymetalist.blogspot.com")
      print(type(foo))

Hasil kode program python:

<table>
  <thead>
    <tr>
      <th> 
      class 'list'<br>
      class 'tuple'
      </th>
    </tr>
  </thead>
</table>


Dalam kode program diatas baris 1 adalah cara pembuatan tipe data List, sedangkan baris 3 adalah cara pembuatan tipe data Tuple.

## Cara Mengakses Tipe Data Tuple Python

Cara mengakses tipe data Tuple tidak berbeda dengan tipe data List, dimana kita menulis nomor urut index dalam tanda kurung siku:

      foo = ("Python", 200, 6.99, True, 'RizkyKhapidsyah', 99j)

      print(foo[0])
      print(foo[1])
      print(foo[2])
      print(foo[2:5])
      print(foo[:3])
      print(foo[3:])
      print(foo[:])

Hasil kode program python:

<table>
  <thead>
    <tr>
      <th> 
      Python
      200
      6.99
      (6.99, True, 'RizkyKhapidsyah')<br>
      ('Python', 200, 6.99)<br>
      (True, 'RizkyKhapidsyah', 99j)<br>
      ('Python', 200, 6.99, True, 'RizkyKhapidsyah', 99j)
      </th>
    </tr>
  </thead>
</table>

Dalam contoh ini saya juga menampilkan cara menampilkan sebagian anggota Tuple. Untuk penjelasan lebih detail anda bisa membaca tutorial tipe data List Python.

 
## Cara Mengganti Nilai Tipe Data Tuple Python

Seperti yang dijelaskan sebelumnya, anggota dari tipe data Tuple tidak bisa diubah atau diganti setelah di definisikan. Benarkah demikian? mari kita coba:

      foo = ("Python", 200, 6.99, True, 'RizkyKhapidsyah', 99j)
      foo[0] = 'Belajar'
      print(foo)

Hasil kode program python:

### Hasil :

<table>
  <thead>
    <tr>
      <th> 
      Traceback (most recent call last):<br>
      File "D:\belajar_python\latihan.py", line 3, in <module><br>
      foo[0] = 'Belajar'<br>
      TypeError: 'tuple' object does not support item assignment</th>
    </tr>
  </thead>
</table>


# List

Kasus: Bagaimana membuat data berkelompok dengan nilai setiap elemennya dapat diubah? List merupakan salah satu tipe data yang ada pada python, terkadang sebagian programmer menyebutnya ‘array-nya’ python. Yah walaupun array pada python sebenarnya ada sendiri. List dibentuk dengan menggunakan tanda bracket atau kurung siku [...]. Dengan list kita bisa menentukan dan mengubah nilai setiap elemennya dengan sesuka hati kita.

      angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      print(angka)

Pada contoh program di atas kita punya variabel angka bertipe list yang memiliki 9 anggota [1-9] atau panjang elemen sebesar 9. Masing-masing anggota angka tersebut bertipe data integer (int). Lantas, bagaimana cara kita mengetahui indeks masing-masing anggota dalam variabel angka dan mengganti salah satu atau dua nilai elemen sekaligus? Karena dalam python indeks suatu data berkelompok dimulai dari 0 maka kita bisa rumuskan sebagai berikut indeks=[data_ke_i – 1]. Misal ingin mencari indeks dari angka 5, maka 5-1=4. Jadi dalam penerapannya kita cukup eksekusi nama_variabel[indeks].

      print(angka[0], angka[4], angka[8])

Setelah kita tahu indeks masing-masing elemen sekarang kita mencoba untuk mengganti nilai elemen tersebut. Caranya sangat mudah kita coba mengganti nilai elemen indeks ke-0 yang bernilai 1 dan indeks ke-8 yang bernilai 9.

      angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      angka[0]=10
      angka[8]=90
      print(angka)

Tapi bagaimana kalau datanya besar? Bagaimana cara kita tahu indeks setiap anggota bila datanya banyak? Solusinya kita dapat menggunakan perulangan for seperti berikut, misal kita punya data sampai angka 100.

      angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
      for data in enumerate(angka):
          print(data)

Nah bisa dilihat di atas kita membuat sebuah perulangan for dengan acuan iterasinya yaitu variabel angka, dalam perulangan tersebut variabel angka kita jadikan parameter pada fungsi enumerate(). Apa kegunaan fungsi enumerate()? Fungsi enumerate() digunakan untuk mengembalikan objek iterasi yang tiap anggotanya berpasangan dengan indeksnya. Fungsi enumerate() ini memiliki 2 parameter, parameter pertama yaitu data iterasi atau data yang dapat diulang seperti list, dictionary, tuple, dan lain-lain. Parameter ke dua adalah nilai awal dari indeks, nilai defaultnya adalah 0. Jadi jika program di atas dijalankan maka akan seperti ini. Angka sebelah kiri merupakan indeksnya sedangkan sebelah kanan adalah data elemen list (indeks, data). Atau saya modifikasi dulu kodingannya menjadi seperti ini.

      angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
      for indeks, data in enumerate(angka):
          print('indeks: ', indeks, '| isinya angka: ', data)

Pada kode di atas tepatnya pada perulangan for saya tambahkan variabel tampungan indeks untuk nantinya menampung indeks data. Apa bisa diakses menggunakan perulangan selain for? while gitu misalnya? Bisa kok.

      indeks = 0
      angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

      while indeks < len(angka):
          print('indeks: ', indeks, '| isinya angka: ' angka[indeks])
          indeks += 1

Jika menggunakan while, mula-mula saya membuat variabel indeks untuk menampung nilai indeks awal. Kemudian pada baris while untuk mendapatkan acuan iterasi saya mengambil berdasarkan jumlah anggota di variabel angka dengan fungsi len(). “Selama nilai variabel indeks masih belum melebihi rule atau syarat jumlah anggota variabel angka: while indeks<len(angka), maka iterasi akan terus dilakukan: indeks += 1. Namun bila melebihi syarat yang ditentukan maka iterasi akan berhenti.” Elemen list tidak harus bernilai bilangan bulat bisa juga menggunakan nilai seperti desimal maupun string.

      angka = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
      for indeks, data in enumerate(angka):
          print('indeks: ', indeks, '| isinya angka: ', data)
          
      kalimat = ['aku suka', 'rikymetalist.blogspot.com', 'maka dari itu', 'aku akan subscribe']
      for data in kalimat:
          print(data, end = " ")

Kode end = " " digunakan untuk menghilangkan enter atau new line setiap kali program menampilkan elemen secara berulang dengan perulangan for.

Hasilnya terjadi error dengan pesan: ‘tuple’ object does not support item assignment, yang kurang lebih berarti: “Tuple tidak mendukung penambahan nilai baru“. Inilah pembeda antara tipe data Tuple dengan tipe data List. Jadi mana yang lebih baik? pilih Tuple atau List? Ini bergantung kepada kebutuhan. Jika kita memiliki data yang isinya tidak boleh diubah, gunakan Tuple. Namun jika data itu nantinya akan diupdate sepanjang kode program, gunakan List.

-----
Referensi Artikel: <a href="https://www.duniailkom.com">DuniaIlkom</a>, <a href="https://belajarpython.com">BelajarPython</a>, <a href="https://kopiding.in">Kopiding.in</a>. Thanks to: <a href="https://www.duniailkom.com">DuniaIlkom</a>, <a href="https://belajarpython.com">BelajarPython</a>, <a href="https://kopiding.in">Kopiding.in</a><br> 
Referensi Source Code Repository: <a href="https://www.youtube.com/user/faqihzamukhlish"> Kelas Terbuka </a> dan <a href="https://github.com/kelasterbuka"> Kelas Terbuka (Repository)</a>. Created by <a href="https://github.com/faqihza">Faqihza Mukhlish.</a> Thanks To: <a href="https://www.youtube.com/channel/UCRGHjysoCemh4y7tCJQs30w/about">Faqihza Mukhlish.</a><br>

-----
All Source Code is Modified.
