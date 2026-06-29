print("teste")

a = 0
n = 1
p = 1

for i in range(10):
    print(p)
    p = n + a
    a = n
    n = p
