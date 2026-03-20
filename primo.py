for i in range(1, 20):
    if i <= 1:
        print(i, "nao primo")
    else:
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        
        if primo:
            print(i, "primo")
        else:
            print(i, "nao primo")
