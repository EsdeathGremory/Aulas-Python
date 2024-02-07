# Class Livro
class Livro:
    def __init__(self, livro, autor):
        self.livro = livro
        self.autor = autor

    def escrito_por(self):
        print(f"O livro com o título {self.livro} foi escrito por {self.autor}.")


livro1 = Livro("No Game No Life", "Yuu Kamiya")
livro2 = Livro("Akame Ga Kill", "Takahiro")
livro3 = Livro("High School DxD", "Ichiei Ishibumi")

livro1.escrito_por()
livro2.escrito_por()
livro3.escrito_por()