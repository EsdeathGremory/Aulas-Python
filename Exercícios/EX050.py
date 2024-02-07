matriz = [[], [], []]
soma = 0
soma2 = 0
maiorNum = 0

for i in range(0, len(matriz)):
    for dados in range(0, 3):
        numero = int(input(f"Insira um numero:"))
        if numero % 2 == 0:
            soma = soma + numero
        if dados == 2:
            soma2 = soma2 + numero
        if i == 2:
            if numero > maiorNum:
                maiorNum = numero

        matriz[i].append(numero)

for i in range(0, 3):
    for v in range(0, 3):
        print(f"{matriz[i][v]}", end=" ")
    print()

print(f"A soma dos numeros pares é: {soma}")
print(f"A soma dos valores da segunda coluna é: {soma2}")
print(f"O maior numero da terceira linha é: {maiorNum}")

