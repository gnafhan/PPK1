A = ['Julie', 'loves', 'me', 'more', 'than', 'Linda', 'loves', 'me']
B = ['Jane', 'likes', 'me', 'more', 'than', 'Julie', 'loves', 'me']
C = A + B
# Fungsi untuk menghitung kemunculan kata di dalam daftar
def count_words(word_list):
    word_counts = {}
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

# Menghitung kata-kata di dalam A dan B
word_counts_A = count_words(A)
word_counts_B = count_words(B)

# Menampilkan tabel dalam format yang rapi
print("{:<10} {:<10} {:<10}".format("Word", "A", "B"))
print("=" * 30)

all_words = set(A + B)

for word in all_words:
    count_A = word_counts_A.get(word, 0)
    count_B = word_counts_B.get(word, 0)
    print("{:<10} {:<10} {:<10}".format(word, count_A, count_B))
    
hasil = 0
pembagiA = 0
pembagiB = 0

for word in all_words:
    hasil += A.count(word)*B.count(word)
    pembagiA += A.count(word)**2
    pembagiB += B.count(word)**2
    
pembagiA = pembagiA**(1/2)
pembagiB = pembagiB**(1/2)
print('Hasil perbandingan:', round((hasil/(pembagiA*pembagiB)),4), sep='\n')

