def calculadora(num1, num2, calcular):
    if calcular == "+":
        print(f"{num1} + {num2} = {num1 + num2}")

    elif calcular == "-":
        print(f"{num1} - {num2} = {num1 - num2}")

    elif calcular == "x":
        print(f"{num1} x {num2} = {num1 * num2}")

    elif calcular == "/":
        print(f"{num1} / {num2} = {num1 / num2}")


def tabuada(num):
    i = 1
    for i in range (1, 11):
        print(f"{num} x {i} = {num * i}")
        i += 1


def par_impar(num):
    if (num % 2) == 0:
        print("Par")
    else:
        print("Ímpar")


def numeros_primos(num):
    if num % 2 == 0:
        print("Número primo.")

    else:
        print("O número não é primo.")


def fatorial(num, mostrar):
    resultado = 1
    count = 1
    show = num
    if mostrar == False:
        while count <= num:
            resultado *= count
            count += 1

        print(resultado)

    elif mostrar == True:
        while count <= num:
            resultado *= count
            if count == num:
                print(f"{show} = ", end="")
            else:
                print(f"{show} x ", end="")
            show -= 1
            count += 1

        print(resultado)
