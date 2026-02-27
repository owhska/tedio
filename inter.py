import tkinter as tk
import random

resposta = random.randint(1,25)

valor = 0
tentativas = 0

def verificar():
    global tentativas
    try:
        valor = int(entrada.get())
        tentativas = tentativas + 1
        
        if (valor > resposta):
            resultado.config(text="valor menor")
        elif (valor < resposta):
            resultado.config(text="valor maior")
        else:
            resultado.config(text=f"Voce acertou e precisou de {tentativas} tentativas")
    except ValueError:
            resposta.config(text="digite um numero valido!")

janela = tk.Tk()
janela.title("Jogo")
janela.geometry("300x300")

"""
entrada.bind("<Return>", verificar)
"""

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Verificar", command=verificar)
botao.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()
