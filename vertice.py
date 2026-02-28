print("calculo de vertice de parabola Xv e Yc")

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

delta = (b ** 2) - (4 * a * c)

xv = (-b) / (2*a)
yv = -(delta) / (4*a)

print(f"Xv = {xv} e Yv = {yv}")
print(f"ou V = ({xv},{yv})")
