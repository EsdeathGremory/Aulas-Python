number = [[], []]
count = 0

for i in range(0, 10):
    numero = int(input(f"Insira o {i + 1}º numero:"))
    if numero % 2 == 0:
        number[0].append(numero)

    else:
        number[1].insert(0, numero)
        count += 1

number[0].sort()
number[1].sort()
print(f"Números ímpares: {number[1]}")
print(f"Números pares: {number[0]}")
