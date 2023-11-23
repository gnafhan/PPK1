data = []
rata2=0
print("== PROGRAM HITUNG RATA-RATA UANG SAKU MAHASISWA ==")
while True:
    nama = input("Masukkan nama : ")
    asal = input("Alamat : ")
    uang = input("Uang saku : ")
    data.append([nama,asal,uang])
    lanjutkan = input("Apakah ingin memasukkan data lagi? (YA/TIDAK) : ").lower() #Ya   
    if(lanjutkan != 'ya'):
        break

print("==== TAMPIL DATA ====")
for i in data:
    print(i[0], end=" ")
    print(i[1], end=" ")
    print(i[2])
print("==== RATA-RATA UANG SAKU MAHASISWA ====")
for i in data:
    rata2 += int(i[2])
print("RATA-RATA UANG SAKU MAHASISWA = ",rata2/len(data))