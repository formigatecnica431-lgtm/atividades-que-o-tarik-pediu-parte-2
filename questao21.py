numero = int(input("Digite um número inteiro:  "))
primo = True

for i in range(2, numero):
    
    if numero % i == 0:
        primo = False
        break
    
    
if primo <= 2:
    print(F"{numero} é primo.")
else:
    print(f"{numero} não é primo")