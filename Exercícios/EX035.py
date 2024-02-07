# EX035

# Recolha de dados
print("[1] - Fazer uma Tabuada:")
print("[2] - Sair")
opcao = int(input("Opção:"))

count = 1

#Calculo da média
while opcao != 2:
    numero = int(input("Introduza o número:"))

    while count <= 10:
        mult = numero * count
        print(f"{count} x {numero} = {mult}")
        count += 1

    count = 1
    print("[1] - Inserir outro número:")
    print("[2] - Sair")
    opcao = int(input("Opção:"))
