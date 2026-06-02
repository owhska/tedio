def ePrimo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

i = 1

for i in range(21):
    if i != 0:

        if ePrimo(i):
            print(f"{i}p")
        else:
            print(i)
