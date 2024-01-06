# Menerima input bilangan dari pengguna
bilangan = float(input("Masukkan sebuah bilangan: "))

# Memeriksa jenis bilangan
if bilangan > 0:
    print("Bilangan positif")
elif bilangan < 0:
    print("Bilangan negatif")
else:
    print("Bilangan nol")

# Memeriksa apakah bilangan merupakan bilangan bulat atau desimal
if bilangan.is_integer():
    print("Bilangan ini adalah bilangan bulat.")
else:
    print("Bilangan ini adalah bilangan desimal.")

# Memeriksa apakah bilangan merupakan bilangan prima atau tidak
if bilangan > 1:
    for i in range(2, int(bilangan)):
        if (bilangan % i) == 0:
            print("Bilangan ini bukan bilangan prima.")
            break
    else:
        print("Bilangan ini adalah bilangan prima.")
else:
    print("Bilangan ini bukan bilangan prima.")
