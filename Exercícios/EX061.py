def maior(*numeros):
    bigger = 0
    for i in numeros[0]:
        if i > bigger:
            bigger = i
    print(f"O maior numero inserido foi: {bigger}")


continuar = "S"
lista = list()

while continuar == "S":
    lista.append(int(input("Insira uma número: ")))
    continuar = input("Deseja continuar? [S/N]: ").upper()

maior(lista)
