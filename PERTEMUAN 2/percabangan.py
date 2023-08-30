def berapaNilai(nilai):
    if(nilai>=85):
        return("Sangat Oke")
    elif(nilai>=70):
        return("Oke")
    elif(nilai>=60):
        return("Lumayan")
    else:
        return("Nice Try")

def inputBaru():
    nilai = int(input("Masukkan nilai: "))
    print(berapaNilai(nilai))

def test ():
    nilai = [50,55,60,65,70,75,80,85,90,95]

    for i in nilai:
        print("Nilai:", i,"||","kategori:", berapaNilai(i))
def main():
    print("Selamat datang di menu pecabangan, tersedia beberapa pilihan:")
    print("1. Menentukan nilai dengan input baru")
    print("2. Menentukan nilai dengan unit test")

    pilihan = int(input("Masukkan nomor (1 atau 2): "))

    if(pilihan ==1):
        inputBaru()
    elif(pilihan == 2):
        test()
    else:
        main()

main()
