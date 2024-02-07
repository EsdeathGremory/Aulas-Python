matriz = [[], [], []]

for i in range(0, len(matriz)):
    for dados in range(0, 3):
        matriz[i].append(input("Insira um numero: "))

for i in range(0, 3):
    for v in range(0, 3):
        print(f"{matriz[i][v]}", end=" ")
    print()
