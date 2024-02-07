# EX041
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
n4 = int(input("Número 4: "))

tuple = (n1, n2, n3, n4)
pares = ""
n5 = False
countN7 = 0

for t in tuple:
    if t == 7:
        countN7 += 1
    if t % 2 == 0:
        pares += str(t) + " - "

if countN7 == 0 and 5 not in tuple and not n5:
    print("Não foram encontrados dados")
else:
    print(f"O número 7 foi inserido: {countN7} vezes.")
    if 5 in tuple:
        n5 = True
        print("O número 5 está na posição.",tuple.index(5))
    if not n5:
        print("O número 5 não foi encontrado.")

    print(f"Os números pares: {pares}")
