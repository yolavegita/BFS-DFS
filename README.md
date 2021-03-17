# BFS-DFS
Source code BFS dan DFS dalam python.


Nama	: Yola Vegita
NPM	: 1184070
Kelas	: D4 Teknik Informatika 3A
MK	: Sistem Pakar
Tugas 2

BFS DAN DFS

1.	BFS (Breadth First Search)

a.	Pengertian

BFS atau bredth first search merupakan sebuah algoritma yang melakukan pencarian secara melebar yang mengunjungi simpul secara preorder yaitu mengunjungi suatu simpul kemudian 
mengunjungi semua simpul yang bertetangga dengan simpul tersebut terlebih dahulu. Kemudian simpul yang belum dikunjungi dan bertetangga dengan simpul simpul yang tadi belum dikunjungi, 
dan seperti itu seterusnya. Apabila graf berbentuk pohon berakar, maka semua simpul pada aras dikunjungi lebih dahulu sebelum simpul-simpul pada aras.

Cara kerja algoritma BFS
Di dalam algoritma BFS, simpul anak yang telah dikunjungi disimpan dalam sebuah antrian. Antrian ini akan digunakan untuk mengacu simpul-simpul yang bertetangga dengannya yang akan 
dikunjungi kemudian sesuai urutan pengantrian. 
Berikut ini adalah langkah-langkah algoritma BFS :

1).	Masukkan simpul ujung (akar) ke dalam antrian.
2).	Ambil simpul dari awal antrian, lalu cek apakah simpul merupakan solusi.
3).	Jika simpul merupakan solusi, pencarian selesai dan hasil dikembalikan.
4).	Jika simpul bukan solusi, masukkan seluruh simpul yang bertetangga dengan simpul tersebut (simpul anak) ke dalam antrian.
5).	Jika antrian kosong dan setiap simpul sudah dicek, pencarian selesai dan mengembalikan hasil solusi tidak ditemukan.
6).	Ulangi pencarian dari Langkah kedua.


b.	Analisis Source Code Di Git Hub

Terdapat sebuah grafik yang menunjukkan jalur seperti berikut :

{'A':set(['B']),

'B':set(['C','A']),

'C':set(['B','H','I','D']),

'D':set(['C','E','H','F']),

'E':set(['D']),

'F':set(['D','G']),

'G':set(['F','H']),

'H':set(['D','C','G','L']),

'I':set(['C','J','K']),

'J':set(['I']),

'K':set(['L','I']),

'L':set(['K','H'])}

Dari jalur tersebut sistem akan menentukan titik mana yang menjadi titik mulai dan juga titik tujuan. Kemudian, jika titik awal adalah titik tujuan, maka sistem akan mengembalikan 
sebuah pesan yaitu “titik mulai merupakan sebuah titik tujuan”. Proses untuk mendapatkan titik tujuan, titik dari jalur yang sudah dipilih dan sudah dikunjungi akan dimasukkan keantrian 
sebelum dimasukkan ke dalam hasil atau result. Lalu sistem akan mengambil titik akhir sebagai tujuan maka akan mengembalikan nilai jalur kedalam antrian.

Apabila titik awal tidak sama dengan tujuan, maka sistem akan mengecek apakah sebuah titik atau node tidak dikunjungi, sistem akan memasukkan semua cabang dari titik graf. Kemudian 
akan dicetak “cabang-“,semuacabang. Selanjutnya sistem akan Kembali mengecek cabang yang tidak dikunjungi, dan memasukkan isi dari variable jalur ke variable jalur baru, update/menambah 
isi dari jalur baru dengan cabang, lalu mencetak “jalur baru-“,jalur_baru. Dalam antrian, akan menambahkan dengan jalur yang baru. Sistem Kembali mengecek, jika cabang sudah sama dengan
tujuan maka akan mengembalikan nilai jalur yang baru.

Sistem juga akan menandai titik mana saja yang sudah dikunjungi, dan titik yang sudah dikunjungi tidak akan bisa kembali dikunjungi. Kemudian jika jalur tidak ditemukan, maka sistem 
akan memberitahukan dengan mencetak “Tidak ada jalur”. Jika sistem sudah selesai melakukan search, maka sistem akan menampilkan atau mencetak start dengan masukkan awal, dan finish 
dengan masukkan akhir dan mencetak jalur yang telah dilalui untuk mendapatkan hasil dari titik tujuan.

Sistem metode BFS, melakukan proses per layer. Misal saja, dalam contoh grafik diatas, A, memiliki jalur ke B yang kemudian B bisa kita masukkan ke dalam antrian dan juga result. 
Setelah itu, kita melihat jalur yang dimiliki oleh B, yaitu A dan C. Dalam BFS, kita dapat langsung memasukkan kedua jalur ini kedalah antrian. Namun karena A sudah ada dalam hasil 
result, maka hanya C yang kita masukkan ke daftar antrian. Kita Kembali mengecek, C memiliki jalur B, H, I dan D. Terkecuali B yang sudah masuk ke dalam antrian dan result, kita hanya 
bisa menambahkan H, I dan D ke dalam antrian. B yang tadinya sudah berada di dalam antrian, dapat kita tambahkan ke dalam result. Dan seperti itu seterusnya, sampai tidak ada lagi titik 
yang tersisa di dalam antrian, dan kemudian titik terakhir yang menjadi hasil, itulah yang menjadi titik tujuan.


2.	DFS (Depth First Search)

a.	Pengertian

DFS merupakan algoritma penelusuran stuktur graf/pohon berdasarkan kedalaman. Simpul ditelusuri dari titik mulai atau root kemudian salah satu simpul yang bertetangga hanya dapat 
ditelusuri salah satunya saja hingga mencapai level terdalam. Saaat penulusuran jalur sudah sampai yang terdalam, maka akan Kembali ke titik awal bertujuan untuk menulusuri titik atau 
tetangga yang laiinya. Dalam implementasi DFS, dapat diselesaikan dengan cara rekursif atau menggunakan bantuan struktur data stack. Stack akan berisi simpul pohon. Berikut sistem 
algoritma dari DFS.

1).	Memasukkan simpul root ke dalam tumpukkan dengan push
2).	Ambil dan simpan isi elemen dari tumpukkan teratas
3).	Hapus isi stack teratas dengan prosedur pop
4).	Periksa apakah simpul pohon yang disimpan tadi memiliki anak simpul
5).	Jika ya, push semua anak simpul yang dibangkitkan ke dalam stack
6).	Jika tumpukkan stack kosong maka berhenti, jika tidak Kembali ke Langkah yang kedua.


b.	Analisis Source Code di Git Hub

Berikut ini grafik atau pohon yang menjadi contoh penerapan DFS

{'A':set(['B']),

'B':set(['C','A']),

'C':set(['B','H','I','D']),

'D':set(['C','E','H','F']),

'E':set(['D']),

'F':set(['D','G']),

'G':set(['F','H']),

'H':set(['D','C','G','L']),

'I':set(['C','J','K']),

'J':set(['I']),

'K':set(['L','I']),

'L':set(['K','H'])}

Sama dengan BFS, DFS juga akan menentukan titik mana yang menjadi titik mulai dan juga titik tujuan. Jjika titik awal adalah titik tujuan, maka sistem akan mengembalikan sebuah pesan 
yaitu “titik mulai merupakan sebuah titik tujuan”. Perbedaanya adalah, jika BFS memasukkan titik yang dikunjungi kedalam antrian, DFS menggunakan struktur data stack. Proses untuk 
mendapatkan titik tujuan, titik dari jalur yang sudah dipilih dan sudah dikunjungi akan dimasukkan keantrian ke dalam data stack, sebelum dimasukkan ke dalam hasil atau result. 
Lalu sistem akan mengambil titik akhir sebagai tujuan maka akan mengembalikan nilai jalur kedalam antrian.

Lalu apabila titik awal tidak sama dengan tujuan, maka sistem akan mengecek apakah sebuah titik atau node tidak dikunjungi, sistem akan memasukkan semua cabang dari titik graf. 
Kemudian akan dicetak “cabang-“,semuacabang. Selanjutnya sistem akan Kembali mengecek cabang yang tidak dikunjungi, dan memasukkan isi dari variable jalur ke variable jalur baru, 
update/menambah isi dari jalur baru dengan cabang, lalu mencetak “jalur baru-“,jalur_baru. Dalam data stack variable akan diupdate atau ditambah dengan jalur yang baru, apabila cabang 
sama dengan tujuan, maka akan mengembalikkan nilai jalur baru.

Sistem juga akan menandai titik mana saja yang sudah dikunjungi, dan titik yang sudah dikunjungi tidak akan bisa kembali dikunjungi. Kemudian jika jalur tidak ditemukan, maka sistem akan
memberitahukan dengan mencetak “Tidak ada titik tersebut dalam graf”. Jika sistem sudah selesai melakukan search, maka sistem akan menampilkan atau mencetak start dengan masukkan awal, 
dan finish dengan masukkan akhir dan mencetak jalur yang telah dilalui untuk mendapatkan hasil dari titik tujuan.

Seperti Namanya DFS atau Depth First Search adalah sebuah metode yang melakukan pencarian sampai level terdalam. Melihat contoh grafik diatas, A yang memiliki jalur ke B dapat langsung 
dimasukkan ke dalam stack dan menjadi sebuah hasil atau result. B yang memiliki dua jalur yaitu A dan C hanya dapat memilih satu jalur untuk melakukan pencarian. Karena A sudah terdapat
dalam data stack dan result, maka B dapat memilih jalur C. C akan masuk ke dalam data stack. Jalur yang dimiliki oleh C adalah B, H, I,  dan D. B yang sudah di dalam data stack tidak 
dapat dipilih. Dari jalur H, I dan D hanya satu yang dapat dipilih sebagai jalur pencarian. Seterusnya seperti itu, sampai titik atau node sudah tidak lagi memiliki jalur. Maka proses 
selanjtnya adalah embali kejalur sebelumnya dengan melihat data paling atas di antrian stack. Jika data stack sudah kosong, saatnya sistem menghentikan proses dan menyimpulkan hasil 
pencarian.

3.	Kesimpulan

Perbedaaan proses kerja dari BFS dan DFS adalah, BFS dapat melakukan pencarian melalui lebih dari satu jalur yang bertetangga dari node. Sedangkan DFS, hanya bisa melalukan pencarian 
menggunakan satu jalur ke bagian terdalam dari sebuah grafik ataupun pohon 

Referensi : http://michaeljulius11.blogspot.com/2017/10/pengertian-metode-pencarian-bfs-dan-dfs.html?m=1


