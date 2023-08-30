def bintang():
    for i in range(int(input("Masukkan baris: "))):
        print("* "* (i+1))
 
 
def bintangKebalik():
    baris = int(input("Masukkan baris: "))
    for i in range(baris):
        print("* " * (baris))
        baris-=1
 
bintangKebalik()