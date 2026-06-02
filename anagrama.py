def anagrama(palavra1, palavra2):

    p1 = palavra1.replace(" ", "").lower()
    p2 = palavra2.replace(" ", "").lower()

    return sorted(p1) == sorted(p2)

if anagrama("listen", "silent"):
    print("true")
else:
    print("false")
