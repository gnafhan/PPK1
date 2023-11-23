# Deklarasi dan inisiasi variabel
data = []
total = 0

# Input data barang harga, apakah akan lanjut atau tidak
print("========== Program kasir sederhana ==========")
while True:
    barang = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    lanjut = input("Apakah anda ingin memasukkan barang lagi? (ya/tidak): ")
    data.append([barang, harga])
    if lanjut.lower() == "tidak":
        break

# Menampilkan daftar belanjaan dan total harga
print("========== Daftar belanjaan ==========")
for i in range(len(data)):
    print(f"{i+1}. {data[i][0]}: {data[i][1]}")

print("========== Total harga ==========")
for i in range(len(data)):
    total += data[i][1]

# Mengecek apakah total harga lebih dari 1 juta atau tidak
if total >= 1000000:
    diskon = "{:,.0f}".format(total*0.05).replace(",", ".")
    total_diskon = "{:,.0f}".format(total*0.95).replace(",", ".")
    total = "{:,.0f}".format(total).replace(",", ".")
    print(f"Total harga: {total} dengan diskon 5% atau {diskon} menjadi {total_diskon}")
    print("Uang yang harus dibayarkan adalah Rp.", total_diskon)
else:
    total = "{:,.0f}".format(total).replace(",", ".")
    print("Uang yang harus dibayarkan adalah Rp", total)