# EX033
# Recolha de dados
print("[1] - Inserir um número")
print("[2] - Sair do programa")
escolha = int(input("Opção:"))

# Variáveis
count = 0
soma = 0

while escolha != 2:
    numero = int(input("Introduza o número:"))
    soma = numero + soma
    count += 1

    print("[1] - Inserir outro número")
    print("[2] - Parar")
    escolha = int(input("Opção:"))

print(f"O Utilizador inserio um valor {count} vezes.")
print(f"A soma dos valores introduzidos é {soma}")
