# EX036

# Bibliotecas
import random

print("------------------------")
print("--Escolha Par ou Ímpar--")
print("------------------------\n")
escolha = int(input("[1] - Par || [2] - Ímpar:"))
numPC = random.randint(1, 10)
vitoria = 0

"""print(f"Número PC:{numPC}")"""

numero = int(input("Insira um número:"))

while escolha != 3:

    if escolha == 1:
        resto = (numero + numPC) % 2

        if resto == 0:
            print("Victory")
            vitoria += 1

        else:
            print("Defeat")
            escolha = 3
            break

    elif escolha == 2:
        resto = (numero + numPC) % 2

        if resto != 0:
            print("Victory")
            vitoria += 1

        else:
            print("Defeat")
            escolha = 3
            break

    numPC = random.randint(1, 10)
    """print(f"Número PC:{numPC}")"""

    escolha = int(input("[1] - Par || [2] - Ímpar:"))
    numero = int(input("Insira um número:"))

print(f"Vitórias consecutivas: {vitoria}.")
