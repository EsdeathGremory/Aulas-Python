"""class Conta:
    def __init__(self, nib, titular, saldo, limite):
        print("A construir objeto...")
        self.nib = nib
        self.titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, valor):
        self.__limite = valor
     """


class Conta:
    def __init__(self, titular, saldo, limite):
        print("Nova conta criada com sucesso...")
        self.titular = titular
        self.__saldo = saldo
        self.limite = limite

    @property
    def saldo(self):
        return f'O saldo da conta é: {self.saldo}'

    @saldo.setter
    def saldo(self, valor):
        if valor > 1000:
            print(f"O valor {valor} é superior ao limite permitido")
        else:
            self.__saldo -= valor


conta = Conta("Ricardo", 1250, 400)
print(conta.saldo)
conta.saldo = 1250
