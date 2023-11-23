baris = int(input())
temp = baris
i = 0
while i < temp:
    print(" "*(baris-1),"* "*(i+1))
    baris-=1
    i+=1
j = 0
while j < temp:
    print(" "*(j+1),"* "*(temp-j-1))
    j+=1

