print ("Nama    : Salsabilla Ahmad")
print ("NIM     : 21343072")
print ("Matkul  : PAA")
print ("Program : Horspool's Algorithm")
# preprocess fungsi yang digunakan untuk membuat tabel pergeseran berdasarkan pattern 
# yang akan dicari
def preprocess(pattern):
# Struktur Inisialisasi tabel pergeseran
    table = {}
    #variabel table melakukan proses pergeseran table
    m = len(pattern)
    table = {}
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i
    return table
# Search fungsi yang digunakan untuk mencari pattern di dalam teks dengan menggunakan tabel pergeseran
# yang sudah dibuat
def search(text, pattern):
#Variabel text dan pattern
            #text variabel yang menyimpan teks yang akan dicari patternnya
            #pattern variabel yang menyimpan pattern yang akan dicari di dalam teks.
    table = preprocess(pattern)
    n = len(text)
    #variabel untuk melakukakan inisialisasi
    m = len(pattern)
    #variabel nilai panjang dari pattern tersebut
    if m > n:
#melakukan pencarian dari indeks terakhir pattern di sebuah teks data tersebut
        return -1
    table = preprocess(pattern)
    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
#menggunakan struktur if while untuk melakukan kombinasi looping pada program tersebut
#dengan menggunakan statement while selama nilai variabel masih kurang dari -1
        if k == m:
            return i - m + 1
        else:
            i += table.get(text[i], m)
#Lakukan pergesaran berdasarkan tabel pergeseran
    return -1

text = "ABBCABBCACB"
#menggunakan variabel teks untuk menyimpan nilai yang akan di pattern kan
pattern = "ACB"
#sedangkan pattern disini akan mencari nilai yang telah kita pattern kan
pos = search(text, pattern)
if pos == -1:
    print("posisi Pada pattern tidak ditemukan")
else:
    print("Pattern ditemukan pada posisi", pos)
