# EX032

# Recolha de dados
numero = int(input("Insira um número inteiro:"))

# Calculo da sequêncian de Fibonacci
count = 0
ultimo = 0
penultimo = 1

while count < numero:
    if numero == 1:
        print(penultimo)

    elif numero == 2:
        print(penultimo)
        count += 1

    else:
        while count < numero:
            soma = ultimo + penultimo
            penultimo = ultimo
            ultimo = soma
            count += 1
            print(soma)
