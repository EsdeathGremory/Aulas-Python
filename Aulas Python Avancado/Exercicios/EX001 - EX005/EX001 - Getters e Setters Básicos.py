from datetime import date


def main():
    anoatual = date.today().year

    class Livro:
        def __init__(self, titulo, autor, ano):
            self.__titulo = titulo
            self.__autor = autor
            self.__ano = ano

        @property
        def titulo(self):
            return self.__titulo

        @titulo.setter
        def titulo(self, valor):
            while valor == "":
                valor = input(f"O título não pode ficar em branco!\nInsira outro nome: ")

            self.__titulo = valor

        @property
        def autor(self):
            return self.__autor

        @autor.setter
        def autor(self, valor):
            while valor == "":
                valor = input(f"O nome do autor não pode ficar em branco!\nInsira outro nome: ")

            self.__autor = valor

        @property
        def ano(self):
            return self.__ano

        @ano.setter
        def ano(self, valor):
            while int(valor) < 1900 or int(valor) > anoatual:
                valor = input(f"O ano do livro tem de ser entre 1900 e a data atual!\nInsira outro ano: ")

            self.__ano = valor

    livro = Livro(None, None, None)
    livro.titulo = input("Titulo: ").strip()
    livro.autor = input("Autor: ").strip()
    livro.ano = int(input("Ano: "))

    print(f"\nTÍTULO: {livro.titulo}")
    print(f"AUTOR: {livro.autor}")
    print(f"ANO: {livro.ano}")


if __name__ == "__main__":
    main()
