class Produto:
    def __init__(self, nome, stock):
        self.nome = nome.strip()
        self.__stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        while valor < 0:
            if valor < 0:
                print(f"O valor não pode ser menor do que 0!")
                valor = int(input("Insira um novo valor: "))

        else:
            self.__stock = valor
            print(f"Stock atualizado\nQUANTIDADE ATUAL: {self.__stock}")

    def mostrar_stock(self):
        print(f"STOCK: {self.__stock}")

    def adicionar_stock(self, valor):
        self.__stock += valor


print("-- Produto --")
Esdeath = input("Clique para adicionar um novo produto...")

nomep = input("NOME: ")
produto = Produto(nomep, None)

produto.stock = int(input("Insira a quantidade de stock: "))
produto.mostrar_stock()
print("A adicionar 1000 unidades...")
produto.adicionar_stock(1000)
produto.mostrar_stock()
