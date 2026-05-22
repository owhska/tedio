import random

print("Voce comeca com 10 fixas")

numeros = [1, 2, 3, 4, 5, 6, 7]
pesos = [1, 1, 1, 1, 1, 1, 3]
fichas = 10
pontuacao = 0
maximo = []
metade = []
minimo = []
comprou = False

def total():
    global pontuacao
    pontuacao += (sum(maximo) + sum(metade) + sum(minimo))*10

    maximo.clear()
    metade.clear()
    minimo.clear()

def comprarFichas():
    global pontuacao, fichas

    total()
    print(f"Voce tem R${pontuacao}")

    if pontuacao == 0:
        exit()

    print("\nVoce deseja comprar mais fichar? (y) (n)")
    op = input("> ")

    if op == "y":
        print("\nCada ficha custa 5 reais\n")
        qt = int(input("Quantas fixas vc deseja comprar? "))

        for i in range(qt):
            pontuacao = pontuacao - 5
            fichas+=1

    else:
        print(f"\nVoce pode sacar R${pontuacao}\n\nBom jogo\n")
        exit()

while True:

    v = int(input("Quantas fichas vc deseja usar? "))

    if v == 0:
        print(f"\nVoce pode sacar R${pontuacao}\n\nVoce manteve {fichas} fichas\n")
        exit()

    for i in range(v):

        if fichas <= 0:
            print("Sem fixas\n")
            comprarFichas()
            comprou = True
            break

        print(f"\nVoce tem {fichas} fichas\n")

        n1 = random.choices(numeros, weights=pesos, k=1)[0]
        n2 = random.choices(numeros, weights=pesos, k=1)[0]
        n3 = random.choices(numeros, weights=pesos, k=1)[0]

        print(f"[{n1}] [{n2}] [{n3}]")

        if n1 == 7 and n2 == 7 and n3 == 7:
            print("Voce ganhou o maximo!!!")
            maximo.append(3)

        elif n1 == 7 and n2 == 7 or n1 == 7 and n3 == 7 or n2 == 7 and n3 == 7:
            print("Voce ganhou metade do valor!!!")
            metade.append(1.5)

        # elif n1 == 7 or n2 == 7 or n3 == 7:
            # print("Voce ganhou o valor minimo :(")
            # minimo.append(0.5)
        else:
            print("Voce nao ganhou nada")

        fichas-=1

    total()
    print(f"\nAgora vc esta com R${pontuacao}\n")
    if fichas <= 0 and pontuacao > 0:
        comprarFichas()
        print(f"\nAgora vc tem R${pontuacao}\n")
        comprou = True

    if comprou:
        comprou = False
        continue

    if fichas <= 0 and pontuacao <= 0:
        print("Fim de jogo")
        break

