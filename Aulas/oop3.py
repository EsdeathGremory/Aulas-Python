class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def __str__(self):
        return (f"Títular: {self.titular}\n"
                f"Saldo: {self.saldo}")


conta_pessoal = ContaBancaria("Ricardo", 1250, 400)
print(conta_pessoal)
