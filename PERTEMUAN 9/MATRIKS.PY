def transpose(ordo):
    matrix = []
    transposed = []
    row, column = list(map(int, ordo.split()))
    for i in range(row):
        matrix.append(list(map(int, input().split())))
    for j in range(len(matrix[0])):
        transposed.append([matrix[i][j] for i in range(len(matrix))])
    for i in transposed:
        for j in i:
            print(j, end=" ")
        print()
transpose(input("masukkan baris dan kolom: (x,y) \n"))
