# EX026
from datetime import date
data_atual = date.today().year
count = 0
count2 = 0
for a in range(0, 7):
    anoNasc = int(input("Insira o ano de nascimento:"))

    idade = data_atual - anoNasc

    if idade >= 18:
        count = count + 1

    else:
        count2 = count2 + 1

print(f"{count} pessoas são maiores de idade.")
print(f"{count2} pessoas são menores de idade.")