def factorial(x=1):
    if x == 1:
        return x
    return x * factorial(x-1)

print(factorial(5))


