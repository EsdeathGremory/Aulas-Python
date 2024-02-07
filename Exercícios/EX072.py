import matemática


def menu():
    opcao = None
    while opcao != 6:
        print("[1] - Calculadora\n[2] - Tabuada\n[3] - Par ou Ímpar\n[4] - Números Primos\n[5] - Factorial\n[6] - Sair")
        opcao = int(input("--->"))
        if opcao == 1:
            try:
                num1 = int(input("Insira o primeiro número:"))
                num2 = int(input("Insira o segundo número"))
                calcular = input("Ensira o sinal da opção que deseja efetuar [+ - x /]:").strip().lower()
                matemática.calculadora(num1, num2, calcular)
                print()

            except ZeroDivisionError:
                print("Não é possível dividir por 0.\n")

            except ValueError:
                print(f"A informação introduzida não é valida.\n")

        if opcao == 2:
            try:
                num = int(input("Insira um número para visualizar a sua tabuada: "))
                matemática.tabuada(num)
                print()

            except ValueError:
                print(f"A informação introduzida não é valida.\n")

        if opcao == 3:
            try:
                num = int(input("Insira um número para saber se é par ou ímpar: "))
                matemática.par_impar(num)
                print()

            except ValueError:
                print(f"A informação introduzida não é valida.\n")

        if opcao == 4:
            try:
                num = int(input("Insira um número inteiro: "))
                matemática.numeros_primos(num)
                print()

            except ValueError:
                print(f"A informação introduzida não é valida.")

        if opcao == 5:
            try:
                num = int(input("Insira um número para saber o seu fatorial: "))
                ver = input("Quer ver os números?\n [Y] - Sim [N] - Não\n-->").strip().upper()
                if ver == "Y":
                    mostrar = True
                if ver == "N":
                    mostrar = False
                matemática.fatorial(num, mostrar)
                print()

            except ValueError:
                print(f"A informação introduzida não é valida.")


menu()
