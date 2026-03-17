import random

con = 1

for con in range(3):
    v1 = random.randint(1,25)
    v2 = random.randint(1,25)

    resultado = v1 * v2

    res = int(input(f"Digite o resultado de {v1} * {v2} = "))

    if (res == resultado):
        print("Voce acertou e ganhou 1 ponto!")
        con = con + 1

    else:
        print("Voce errou, mas continue tentando")

print(f"O jogo acabou e sua pontuacao foi {con}")
