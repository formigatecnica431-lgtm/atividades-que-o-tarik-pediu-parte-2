numero = int(input("Digite um número inteiro:  "))

for n in range(1,numero+1):
    primo = True

    for i in range(2, n):
    
        if n % i == 0:
            primo = False
            break
    
    
    if primo:
        print(F"{n} é primo.")
    else:
        print(f"{n} não é primo")