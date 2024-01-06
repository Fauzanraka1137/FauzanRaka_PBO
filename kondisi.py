# Menerima input umur dari pengguna
umur = int(input("Masukkan umur Anda: "))

# Memeriksa kategori umur
if umur < 0:
    print("Umur tidak valid.")
elif umur < 18:
    print("Anda masih di bawah umur.")
elif umur < 65:
    print("Anda adalah seorang dewasa.")
else:
    print("Anda sudah masuk kategori lansia.")
