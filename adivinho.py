import random

resposta = random.randint(1,25)

valor = 0
tentativas = 0

while(valor != resposta):
    if(valor != None):
        if(valor > resposta):
            print("valor menor")
        else:
            print("valor maior")

        valor = int(input("Qual o numero secreto?\n"))
        tentativas = tentativas + 1

print(f"Voce acertou!!! Parabens!!!\n");
print(f"Voce acertou em {tentativas} tentativas!")
