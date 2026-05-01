import random


numero = random.randint(1, 10)
contador = 0

while True:

    contador = contador + 1

    v = int(input("Digite um numero: "))

    if v < numero:
        print("Numero maior")
    elif v > numero:
        print("Numero menor")

    elif v == numero:
        print("voce acertou!\n")
        print(f"Voce precisou de {contador} tentativas!")
        break
