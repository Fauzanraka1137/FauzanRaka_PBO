import math

def hitung_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

def hitung_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    sisi_miring = math.sqrt((alas ** 2) + (tinggi ** 2))
    keliling = alas + tinggi + sisi_miring
    return luas, keliling

def hitung_lingkaran(jari_jari):
    luas = math.pi * (jari_jari ** 2)
    keliling = 2 * math.pi * jari_jari
    return luas, keliling

# Fungsi untuk meminta input dari pengguna
def input_persegi():
    sisi = float(input("Masukkan panjang sisi persegi: "))
    hasil_luas, hasil_keliling = hitung_persegi(sisi)
    print(f"Luas persegi: {hasil_luas}")
    print(f"Keliling persegi: {hasil_keliling}")

def input_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    hasil_luas, hasil_keliling = hitung_persegi_panjang(panjang, lebar)
    print(f"Luas persegi panjang: {hasil_luas}")
    print(f"Keliling persegi panjang: {hasil_keliling}")

def input_segitiga():
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    hasil_luas, hasil_keliling = hitung_segitiga(alas, tinggi)
    print(f"Luas segitiga: {hasil_luas}")
    print(f"Keliling segitiga: {hasil_keliling}")

def input_lingkaran():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    hasil_luas, hasil_keliling = hitung_lingkaran(jari_jari)
    print(f"Luas lingkaran: {hasil_luas}")
    print(f"Keliling lingkaran: {hasil_keliling}")

# Meminta pengguna untuk memilih bangun datar
print("Pilih bangun datar:")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Segitiga")
print("4. Lingkaran")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == '1':
    input_persegi()
elif pilihan == '2':
    input_persegi_panjang()
elif pilihan == '3':
    input_segitiga()
elif pilihan == '4':
    input_lingkaran()
else:
    print("Pilihan tidak valid.")
