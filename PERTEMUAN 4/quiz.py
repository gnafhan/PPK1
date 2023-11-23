x = input()
output = 0
length = len(x)-1
for i in x:
    output += int(i)*(2**length)
    length -= 1

print(output)
