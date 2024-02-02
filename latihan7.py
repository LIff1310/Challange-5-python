print("LATIHAN 7")

print("-"*20)
print("Kode Kota : ")
print("1. Prabumulih ")
print("2. Muara Enim ")
print("3. Lubuk Linggau ")
kota = int(input("Pilihan Kota (1,2,3) : "))

if kota == 1:
    print("Kode Kelas : ")
    print("1. Ekonomi ")
    print("2. Bisnis ")
    print("3. Eksekutif ")
    kelas = int(input("Pilihan Kelas (1,2,3) : "))
    if kelas == 1:
        kelas = 100000
    elif kelas == 2:
        kelas = 400000
    elif kelas == 3:
        kelas = 700000

if kota == 2:
    print("Kode Kelas : ")
    print("1. Ekonomi ")
    print("2. Bisnis ")
    print("3. Eksekutif ")
    kelas = int(input("Pilihan Kelas (1,2,3) : "))
    if kelas == 1:
        kelas = 200000
    elif kelas == 2:
        kelas = 500000
    elif kelas == 3:
        kelas = 800000

if kota == 3:
    print("Kode Kelas : ")
    print("1. Ekonomi ")
    print("2. Bisnis ")
    print("3. Eksekutif ")
    kelas = int(input("Pilihan Kelas (1,2,3) : "))
    if kelas == 1:
        kelas = 300000
    elif kelas == 2:
        kelas = 600000
    elif kelas == 3:
        kelas = 900000

tiket = int(input("Jumlah Tiket : "))

subtotal = tiket * kelas
kodepromo = (input("Masukan Diskon : "))
if kodepromo == "igs":
    diskon = 0.10 * subtotal

print("-"*20)

print(f"Harga Tiket : {kelas}")

print(f"Subtotal : {subtotal}")

print(f"Diskon : {diskon:>.0f}")

totalbayar = subtotal - diskon
print(f"Total Bayar : {totalbayar:>.0f}")