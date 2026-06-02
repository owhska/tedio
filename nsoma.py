lista = [4, 2, 3, 4]

N = 7

for i in range(len(lista)):
    for j in range(i+1, len(lista)):

        if lista[i] + lista[j] == N:
            print(f"Valores da posicao {i} e {j}")

