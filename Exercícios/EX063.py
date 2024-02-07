def tabuada(num):
    count = 1
    while True:
        print(f"{num} * {count} = {num * count}")
        count += 1
        if count == 11:
            break


numero = int(input("Insira uma número para ver a sua tabuada:"))
tabuada(numero)
