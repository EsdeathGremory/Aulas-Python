# Criar uma conta bancária
# Identidade, títular, saldo, Limite
# Levantar dinheiro, depositar dinheiro, extrato
"""def levantar_dinheiro(valor):
    if valor > conta["Limite"]:
        print(f"O seu limite é de {conta["Limite"]}.")

    if conta["Saldo"] > valor:
        conta["Saldo"] -= valor


def depositar_dinheiro(valor):
    conta["Saldo"] += valor


def extrato():
    print(f"A conta {conta["identidade"]} tem o saldo de {conta["Saldo"]}.")


conta = {"identidade": input("ID: "),
        "Títular": input("Títular: "),
        "Saldo": int(input("Saldo: ")),
        "Limite": int(input("Limite: "))}"""

# OOP


class Conta:
    def __init__(self, identidade, titular, saldo, limite):
        self.identidade = identidade
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def levantar(self, valor):
        if valor > self.limite:
            print(f"O seu limite é de {self.limite}.")

        if self.saldo > valor:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def extrato(self):
        print(f"A conta {self.identidade} tem {self.saldo}€ desponíveis.")


conta = Conta("123Ric", "Ricardo", 1000, 400)

conta.extrato()
