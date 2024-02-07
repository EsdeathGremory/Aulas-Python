# Class Livro
class Livro:
    def __init__(self, livro, autor):
        self.livro = livro
        self.autor = autor

    def livro_ver(self):
        print(f"{self.livro} | {self.autor}")
        print("-------------------------")


livro1 = Livro("No Game No Life", "Yuu Kamiya")
livro2 = Livro("Akame Ga Kill", "Takahiro")
livro3 = Livro("High School DxD", "Ichiei Ishibumi")

livro1.livro_ver()
livro2.livro_ver()
livro3.livro_ver()
