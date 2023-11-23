bilangan = int(input())
def Prima(bilangan):
    i = 2
    while i<bilangan:
        if(bilangan%i==0):
            return "Bukan prima"
        i+=1
    return "Prima"
    
print(Prima(bilangan))