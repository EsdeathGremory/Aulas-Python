# EX031

# Recolha de dados
numero = int(input("Insira um numero para calcular o seu fatorial:"))

fatorial = 1
count = numero

# Calculo do fatorial
while count > 0:
    print(f"{count}", end="")
    print(" x " if count > 1 else " = ", end="")
    fatorial *= count
    count -= 1

print(f"{fatorial}")

"""for count in range(1, numero + 1):
    fatorial *= count

print(f"O fatorial de {numero} é {fatorial}.")"""
