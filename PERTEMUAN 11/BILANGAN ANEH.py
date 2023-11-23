def aneh (x):
    if x<=3:
        return 1
    else:
        return aneh(x-1)+aneh(x-2)+aneh(x-3)
    

def bukanRekursif(x):
    if x<=3:
        return 1
    else:
        a,b,c=1,1,1
        for i in range (x-3):
            d=a+b+c
            a=b
            b=c
            c=d
        return d
    

for i in range(1,8):
    print(i, aneh(i), bukanRekursif(i))