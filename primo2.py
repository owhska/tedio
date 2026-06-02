def ePrimo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

valor = int(input("Verificar primo: "))

if ePrimo(valor):
    print(f"{valor} e primo")
else:
    print(f"{valor} nao e primo")
