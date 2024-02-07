# EX037
# Recolha de dados
escolha = int(input("[1] - Registar pessoa [2] - Sair\n"))

count25 = 0
countH17 = 0
countM = 0
countUnder = 0

while escolha == 1:
    idade = int(input("Idade:"))
    sexo = int(input("[1]- Masculino [2] - Feminino\n"))
    if idade > 25:
        count25 += 1
    elif idade < 17 and sexo == 1:
        countH17 += 1
    elif sexo == 2:
        countM += 1
    if idade < 18:
        countUnder += 1

    escolha = int(input("[1] - Continuar [2] - Sair\n"))

print(f"Dos dados introduzidos {count25} têm mais de 25 anos.")
print(f"Dos dados introduzidos {countH17} são homens com menos de 17 anos.")
print(f"Dos dados introduzidos {countM} são mulheres.")
print(f"Dos dados introduzidos {countUnder} são menores de idade.")