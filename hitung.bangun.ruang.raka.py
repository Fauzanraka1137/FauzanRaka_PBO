import math

def hitung_kubus(sisi):
    volume = sisi ** 3
    luas_permukaan = 6 * (sisi ** 2)
    return volume, luas_permukaan

def hitung_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    return volume, luas_permukaan

def hitung_tabung(jari_jari, tinggi):
    volume = math.pi * (jari_jari ** 2) * tinggi
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return volume, luas_permukaan

def hitung_bola(jari_jari):
    volume = (4/3) * math.pi * (jari_jari ** 3)
    luas_permukaan = 4 * math.pi * (jari_jari ** 2)
    return volume, luas_permukaan

# Fungsi untuk meminta input dari pengguna
def input_kubus():
    sisi = float(input("Masukkan panjang sisi kubus: "))
    hasil_volume, hasil_luas_permukaan = hitung_kubus(sisi)
    print(f"Volume kubus: {hasil_volume}")
    print(f"Luas permukaan kubus: {hasil_luas_permukaan}")

def input_balok():
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    hasil_volume, hasil_luas_permukaan = hitung_balok(panjang, lebar, tinggi)
    print(f"Volume balok: {hasil_volume}")
    print(f"Luas permukaan balok: {hasil_luas_permukaan}")

def input_tabung():
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    hasil_volume, hasil_luas_permukaan = hitung_tabung(jari_jari, tinggi)
    print(f"Volume tabung: {hasil_volume}")
    print(f"Luas permukaan tabung: {hasil_luas_permukaan}")

def input_bola():
    jari_jari = float(input("Masukkan jari-jari bola: "))
    hasil_volume, hasil_luas_permukaan = hitung_bola(jari_jari)
    print(f"Volume bola: {hasil_volume}")
    print(f"Luas permukaan bola: {hasil_luas_permukaan}")

# Meminta pengguna untuk memilih bangun ruang
print("Pilih bangun ruang:")
print("1. Kubus")
print("2. Balok")
print("3. Tabung")
print("4. Bola")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == '1':
    input_kubus()
elif pilihan == '2':
    input_balok()
elif pilihan == '3':
    input_tabung()
elif pilihan == '4':
    input_bola()
else:
    print("Pilihan tidak valid.")
