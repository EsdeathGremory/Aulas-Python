# EX046

lista = list()
pares = list()
impares = list()
s = "s"

while s != "N":

    num = int(input("Insira um número:"))
    lista.append(num)

    if num % 2 == 0:
        pares.append(num)

    else:
        impares.append(num)

    s = str(input("Quer continuar? [S/N]:")).upper()

print(f"Todos os números inseridos: {lista}.")
print(f"Todos os números pares: {pares}.")
print(f"Todos os números impares: {impares}.")
