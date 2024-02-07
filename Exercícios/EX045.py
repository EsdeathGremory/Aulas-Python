# EX045

lista = list()

for c in range(0, 5):
    num = int(input("Insira um número:"))

    if c == 0:
        lista.append(num)

    elif num > lista[-1]:
        lista.append(num)

    else:
        count = 0
        while count < len(lista):
            if num <= lista[count]:
                lista.insert(count, num)
                break
            count += 1

print(f"Os valores introduzidos são: {lista}.")



