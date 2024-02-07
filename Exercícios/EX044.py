# EX044

continuar = str(input("Quer inserir um numero? [S/N]")).upper()
lista = list()

while continuar != "N":
    num = int(input("Insira o número:"))

    if num in lista:
        print("Número já introduzido.")
        continuar = str(input("Quer inserir outro numero? [S/N]")).upper()

    lista.append(num)
    continuar = str(input("Quer inserir outro numero? [S/N]")).upper()

lista.sort(reverse=True)
print(lista)
