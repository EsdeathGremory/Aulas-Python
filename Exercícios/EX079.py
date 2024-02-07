class ContaBancaria:
    def __init__(self, nib, titular, saldo, limite):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_nib(self):
        return self.__nib

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_saldo(self, valor):
        self.__saldo += valor
        print(f"Saldo atualizado para: {self.__saldo}")

    def set_saldo_levantar(self, valor):
        if valor > self.__limite:
            print("O valor introduzido passa do limite.")

        elif valor <= self.__limite:
            self.__saldo -= valor
            print(f"Saldo atualizado para: {self.__saldo}")

    def set_limite(self, valor):
        self.__limite = valor
        print(f"Novo limite defenido para: {self.__limite}")


nib1 = int(input("Insira o NIB da conta: "))
titular1 = input("Insira o nome do titular: ")
saldo1 = float(input("Insira o saldo da conta:"))
limite1 = float(input("Insira o saldo da conta: "))

conta = ContaBancaria(nib1, titular1, saldo1, limite1)

opcao = None
while opcao != 4:
    opcao = int(input("[1] - Depositar\n[2] - Atualizar limite\n[3] - Levantar\n[4] - Sair\n-->"))
    if opcao == 1:
        print(f"O saldo atual é: {conta.get_saldo()}")
        valor1 = float(input("Insira o valor a adicionar: "))
        conta.set_saldo(valor1)
        print(f"O saldo atual é: {conta.get_saldo()}\n")

    if opcao == 2:
        print(f"O limite atual é: {conta.get_limite()}")
        valor1 = float(input("Insira o novo limite: "))
        conta.set_limite(valor1)
        print(f"O limite atualizado é: {conta.get_limite()}\n")

    if opcao == 3:
        print(f"O saldo atual é: {conta.get_saldo()}")
        valor1 = float(input("Insira o valor a levantar: "))
        conta.set_saldo_levantar(valor1)
        print(f"O saldo atual é: {conta.get_saldo()}\n")
