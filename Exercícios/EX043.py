# EX043

n0 = int(input("Número 1: "))
n1 = int(input("Número 2: "))
n2 = int(input("Número 3: "))
n3 = int(input("Número 4: "))
n4 = int(input("Número 5: "))

lista = [n0, n1, n2, n3, n4]

print(f"O maior valor dos números introduzidos é {max(lista)} e está na posição: {lista.index(max(lista))}.")
print(f"O menor valor dos números introduzidos é {min(lista)} e está na posição: {lista.index(min(lista))}.")
