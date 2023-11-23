def bukan_join_anjer(teks,pisah =False):
    hasil = ""
    for i in teks:
        hasil += i
        if pisah:
            hasil += " "
    return hasil

def petik(teks):
    teks = list(teks)
    for i in range(len(teks)):
        if i % 2 == 0:
            if i+1> len(teks)-1:
                continue
            teks[i], teks[i+1] = teks[i+1], teks[i]
    return bukan_join_anjer(teks)

def bintang(teks):
    teks = list(teks)
    teks = teks[::-1]
    return  bukan_join_anjer(teks)

def encode(teks):
    kata = []
    hasil = []
    for i in teks:
        if i =="^":
            hasil = [*hasil, petik(bukan_join_anjer(kata))]
            kata = []
        elif i == "*":
            hasil = [*hasil, bintang(bukan_join_anjer(kata))]
            kata = []
        else:
            kata = [*kata, i]
    return bukan_join_anjer(hasil, True)

print(encode("ini^adalah*contoh*kata^rahasia*"))