plat = input("Masukkan plat nomor: ")
asal_kota = plat[0]
real_digit = int(input("Masukkan jumlah digit: "))
real_huruf = int(input("Masukkan banyak digit: "))
jumlah_digit = 0
jumlah_huruf = 0
for i in plat[1:]:
    if i.isdigit():
        jumlah_digit += int(i)
        jumlah_huruf += 1


print(jumlah_digit, jumlah_huruf)
if asal_kota == "D":
    if real_digit == jumlah_digit and real_huruf == jumlah_huruf:
        print("Mobil Tuan Kil ditemukan !")
    else:
        print("Bukan mobil Tuan Kil!")
else:
    print("Bukan mobil Tuan Kil!")