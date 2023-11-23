def quick_sort(arr): #deklarasi fungsi yang menerima parameter arr yaitu sebuah list
    if len(arr)<=1: # basis jika panjang list hanya 1
        return arr #akan mengembalikan list itu sendiri
    else:
        pivot = arr.pop(0) #mengambil pivot yaitu element pertama pada array
        pivot_lower = [] # deklarasi list penyimpan element yang kurang dari pivot
        pivot_higher = [] # deklarasi list penyimpan element yang lebih dari sama dengan pivot
        for i in arr: # deklarasi perulangan untuk setiap element
            if i < pivot: # jika elemen kurang dari pivot
                pivot_lower.append(i) # maka memasukkan elemen ke dalam list pivot_lower
            else: # jika elemen lebih dari sama dengan pivot
                pivot_higher.append(i) # maka elemen di masukkan kedalam list pivot_higher
        return quick_sort(pivot_lower) + [pivot] + quick_sort(pivot_higher) # memasukkan list pivot_lower dan pivot_higher kedalam rekurens serta menggabungkan sehingga menjadi hasil akhir 
print(quick_sort([2,4,5,6,2,3,6,1,8,2,2,9,1,0,2,1,7,9,2,4])) # memanggil fungsi dan memprintnya