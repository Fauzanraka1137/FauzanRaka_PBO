# Menerima input string dari pengguna
input_string = input("Masukkan sebuah string: ")

# Menampilkan panjang string
panjang_string = len(input_string)
print(f"Panjang string: {panjang_string}")

# Menampilkan string dalam huruf kapital
string_kapital = input_string.upper()
print(f"String dalam huruf kapital: {string_kapital}")

# Menampilkan string dalam huruf kecil
string_kecil = input_string.lower()
print(f"String dalam huruf kecil: {string_kecil}")

# Memisahkan string berdasarkan spasi
kata = input_string.split()
print(f"Pemisahan kata: {kata}")

# Menggabungkan string dengan pemisah tertentu
pemisah = input("Masukkan pemisah untuk menggabungkan kata (misalnya, spasi atau tanda -): ")
string_gabung = pemisah.join(kata)
print(f"Gabungan kata: {string_gabung}")

# Memeriksa apakah string merupakan palindrom atau tidak
if input_string == input_string[::-1]:
    print("String ini adalah palindrom.")
else:
    print("String ini bukan palindrom.")
