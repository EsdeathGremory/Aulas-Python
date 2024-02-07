class Produto:
    def __init__(self, nome, quantidade_stock):
        self.nome = nome
        self.qs = quantidade_stock

    def mostrar(self):
        print(f"O produto '{self.nome}' tem {self.qs} unidades em stock.")

    def adicionar(self, add):
        self.qs += add


produto = Produto("No Game No Life", 500)

produto.mostrar()

num = int(input("Quantas unidades vão ser adicionadas: "))
produto.adicionar(num)
produto.mostrar()
