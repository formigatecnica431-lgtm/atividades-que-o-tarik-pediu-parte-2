nome = ""
idade = 0
salario = 0
estado_civil = ""
sexo = ""





while True:
    nome = input("Digite o nome: ")
    if len(nome) > 3:
        break
    else:
        print("Erro digite um nome com mais de 3 caracteres ")
    print()
while True:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        
        else:
            print("Erro Digite uma idade valida.")
while True:
        salario = float(input("Digite seu salario atual: "))
        if salario > 0:
            break
        else:
           print("Erro digite um salario maior que 0.")
while True:
        sexo = input("Digite sua idade (F/M): ").lower()
        if sexo == "f" or sexo == "m":
         break
        else:
          print("Erro digite F ou M para continuar.")
while True:
        estado_civil = input("Digite o estado civil (s/c/v/d): ").lower()
        if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
         break
        else:
         print("Digite um estado civil valido.")

print(f"""
------------CADASTRO FEITO COM SUCESSO------------
nome:{nome}
idade:{idade}
sexo:{sexo}
salario:{salario}
estado civil:{estado_civil}





""")