# for n in range(100):
#     if(n%2==1):
#         print("Weird", n)
#     elif((n%2==0 and n<6)):
#         print("Not Weird", n)
#     elif (n%2==0 and n<20):
#         print("Weird", n)
#     elif (n%2==0 and n>20):
#         print("Not Weird", n)


# def keliling(x):
#     for i in range(x):
#         if i in [0,x-1] :
#             print("#"*x)
#         else:
#             print("#"," "*(x-4),"#")
# keliling(4)

# for n in range(100):
#     if n % 2 == 1:
#         print("Weird", n)
#     elif n % 2 == 0 and 2 <= n <= 5:
#         print("Not Weird", n)
#     elif n % 2 == 0 and 6 <= n <= 20:
#         print("Weird", n)
#     elif n % 2 == 0 and n > 20:
#         print("Not Weird", n)


x = int(input(""))
i = 1
while i<x:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1