soma = 0

for i in range(5):
    numero = float(input("Digite um número: "))
    soma += numero

media = soma / 5

print(f"Soma é:{soma}")
print(f"Média é:{media}")