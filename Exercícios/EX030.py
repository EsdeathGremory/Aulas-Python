# EX030

# Menu do programa
print("[1] - Soma")
print("[2] - Multiplicar")
print("[3] - Maior")
print("[4] - Novos Números")
print("[5] - Sair do programa")
opcao = int(input("Escolha a opção:"))

if 5 <= opcao <= 1:
    opcao = int(input("Insira uma opção válida:"))

# Recolha dos valores
valor1 = int(input("Insira o primeiro valor:"))
valor2 = int(input("Insira o segundo valor:"))
valor3 = int(input("Insira o terceiro valor:"))

# Loop do programa
while opcao != 5:

# Calculo de dados dependente da opção escolhida
    if opcao == 1:
        # Soma
        soma = valor1 + valor2 + valor3
        print(f"A soma dos valores introduzidos é: {soma}.")
        print("")

        print("[1] - Soma")
        print("[2] - Multiplicar")
        print("[3] - Maior")
        print("[4] - Novos Números")
        print("[5] - Sair do programa")
        opcao = int(input("Escolha a opção:"))

    elif opcao == 2:
        # Multiplicação
        mult = valor1 * valor2 * valor3
        print(f"A multiplicação dos 3 valores introduzidos é: {mult}.")
        print("")

        print("[1] - Soma")
        print("[2] - Multiplicar")
        print("[3] - Maior")
        print("[4] - Novos Números")
        print("[5] - Sair do programa")
        opcao = int(input("Escolha a opção:"))

    elif opcao == 3:
        # Maior valor
        if valor1 > valor2 and valor1 > valor3:
            print(f"O maior número introduzido foi:{valor1} .")
            print("")

        elif valor2 > valor1 > valor3:
            print(f"O maior número introduzido foi:{valor2} .")
            print("")

        else:
            print(f"O maior número introduzido foi:{valor3} .")
            print("")

        print("[1] - Soma")
        print("[2] - Multiplicar")
        print("[3] - Maior")
        print("[4] - Novos Números")
        print("[5] - Sair do programa")
        opcao = int(input("Escolha a opção:"))

    elif opcao == 4:
        # Recolha dos valores
        valor1 = int(input("Insira o primeiro valor:"))
        valor2 = int(input("Insira o segundo valor:"))
        valor3 = int(input("Insira o terceiro valor:"))
        print("")

        print("[1] - Soma")
        print("[2] - Multiplicar")
        print("[3] - Maior")
        print("[4] - Novos Números")
        print("[5] - Sair do programa")
        opcao = int(input("Escolha a opção:"))
