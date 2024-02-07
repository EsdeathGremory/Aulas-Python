class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def titular(self):
        return f"TITULAR: {self.__titular}"

    @titular.setter
    def titular(self, novo_nome):
        self.__titular = novo_nome

    @property
    def saldo(self):
        return f"SALDO: {self.__saldo}"

    @saldo.setter
    def saldo(self, valor=0):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Valor inválido para saldo. Deve ser não-negativo.")

    @property
    def limite(self):
        return f"LIMITE: {self.__limite}"

    @limite.setter
    def limite(self, valor=400):
        self.__limite = valor

    def depositar(self, valor):
        self.__saldo += valor
        print(f"{valor}€ depositado com sucesso\nSaldo atual {self.__saldo}€.\n")

    def sacar(self, valor):
        if valor <= self.__limite:
            self.__saldo -= valor
            print(f"{valor}€ levantados com sucesso\nSaldo atual {self.__saldo::saldo}€.\n")

        else:
            print(f"{valor}€ excede o limite diário de {self.__limite}€.")


conta = ContaBancaria("Shiro", 10000, 400)

num = int(input("Quantidade de dinheiro a depositar: "))
conta.depositar(num)

num = int(input("Quantidade de dinheiro para levantar: "))
conta.sacar(num)
