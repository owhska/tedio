def palindromo(texto):
    texto = texto.lower()
    invertida = texto[::-1]

    i = invertida.replace(" ", "")
    t = texto.replace(" ", "")

    return i == t

if palindromo("ame o poema"):
    print("p")
else:
    print("n p")
