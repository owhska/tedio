
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

delta = (b ** 2) - (4 * a * c)

raizDelta = delta**0.5

if delta < 0:
    print("inexiste raiz real")
elif delta == 0:
    print("soente uma raiz")

    x1 = (-b + raizDelta) / (2*a)
    print(f"x = {x1}")
else:

    print("duas raizes")

    x1 = (-b + raizDelta) / (2*a)
    x2 = (-b - raizDelta) / (2*a)
    print(f"x1 = {x1} e x2 = {x2}")
