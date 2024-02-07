# EX027

maior_idade = 0
menor_idade = 0
for a in range(0, 10):
    idade = int(input("Insira uma idade:"))

    if maior_idade <= idade:
        maior_idade = idade

    elif menor_idade == 0 or menor_idade >= idade:
        menor_idade = idade

print(f"A maior idade introduzida foi {maior_idade}.")
print(f"A menor idade introduzida foi {menor_idade}.")