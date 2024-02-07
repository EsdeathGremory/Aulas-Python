class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor
        print(f"{valor}€ depositado com sucesso\nSaldo atual {self.saldo}€.\n")

    def sacar(self, valor):
        if valor <= self.limite:
            self.saldo -= valor
            print(f"{valor}€ levantados com sucesso\nSaldo atual {self.saldo}€.\n")

        else:
            print(f"{valor}€ excede o limite diário de {self.limite}€.")


conta = ContaBancaria("Shiro", 10000, 400)

num = int(input("Quantidade de dinheiro a depositar: "))
conta.depositar(num)

num = int(input("Quantidade de dinheiro para levantar: "))
conta.sacar(num)
