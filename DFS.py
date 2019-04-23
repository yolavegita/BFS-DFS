#DFS
#4617

peta1 = {'A':set(['B']),
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


def dfs(graf, awal, tujuan):
    stack = [[awal]]
    dikunjungi = []

    # Cek apabila apakah titik mulai adalah titik tujuan
    if awal == tujuan:
        return"Titik mulai merupakan sebuah tujuan"

    while stack:
        # Memasukkan antrian paling depan ke variabel jalur
        jalur = stack.pop(-1)
        print("Jalur -",jalur)
        # Mengambil titik yang berada di akhir dari jalur
        titik = jalur[-1]
        print("node -",titik)
        # Jika titik awal tidak sama dengan tujuan, maka cek apakah titik tidak ada di dikunjungi
        if titik == tujuan:
            return jalur
        # Jika titik tidak ada di dikunjungi, maka cek cabang
        elif titik not in dikunjungi:
            semuacabang = graf[titik] #Memasukan semua cabang dari titik graf kedalam semua
            print("Cabang -",semuacabang)
            for cabang in semuacabang: #cek semua cabang dari titik
                jalur_baru = list(jalur) #Memasukan isi dari vaariabel jalur ke variabel jalur baru
                jalur_baru.append(cabang) #Update/tambah isi dari jalur baru dengan cabang
                print("Jalur baru -",jalur_baru)
                stack.append(jalur_baru) #Update/tambah isi dari stack dengan jalur baru
                #Mengecek cabang apakah sama dengan tujuan, jika sama maka return nilai jalur baru
                 

            dikunjungi.append(titik) #Menandai titik yang sudah dikunjungi sebagai dikunjungi
            print("Kunjungan -",dikunjungi)
    # Apabila tidak ditemukan jalur, titik yang diinputkan tidak ada
    print("Tidak ada titik tersebut dalam graf!")


start = input("Masukan awal: ")
finish = input("Masukan Akhir: ")

print("Jalur yang dilalui : ",dfs(peta1, start, finish))
