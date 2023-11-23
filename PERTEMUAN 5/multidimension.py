ordo = input().split()
panjang =  int(ordo[0])
lebar = int(ordo[1])
m_list = [0]*panjang

for i in range(panjang):
    m_list[i] = list(map(int, input().split()))

balik = m_list[::-1]
rotasi = [0]*lebar

temp = []
for i in range(lebar):
    x = i
    for k in balik:
        temp.append(k[i])
    rotasi[i]= temp
    temp = []


for i in rotasi:
    for j in i:
        print(j, end=" ")
    print()

