baris = int(input("Masukkan angka: "))
i = 0
while i< baris:
    if i in [0,baris-1]:
        print("*"*baris)
    else:
        print("*", " "* (baris-4), "*")
    i+=1