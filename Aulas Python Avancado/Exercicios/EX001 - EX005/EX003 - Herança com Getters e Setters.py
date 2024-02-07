from datetime import date


def main():
    anoatual = date.today().year

    class Livro:
        def __init__(self, titulo, autor, ano):
            self._titulo = titulo
            self._autor = autor
            self._ano = ano

        @property
        def titulo(self):
            return self._titulo

        @titulo.setter
        def titulo(self, valor):
            while valor == "":
                valor = input(f"O título não pode ficar em branco!\nInsira outro nome: ")

            self._titulo = valor

        @property
        def autor(self):
            return self._autor

        @autor.setter
        def autor(self, valor):
            while valor == "":
                valor = input(f"O nome do autor não pode ficar em branco!\nInsira outro nome: ")

            self._autor = valor

        @property
        def ano(self):
            return self._ano

        @ano.setter
        def ano(self, valor):
            while int(valor) < 1900 or int(valor) > anoatual:
                valor = input(f"O ano do livro tem de ser entre 1900 e a data atual!\nInsira outro ano: ")

            self._ano = valor

    class Ebook(Livro):
        def __init__(self, titulo, autor, ano):
            super().__init__(titulo, autor, ano)
            self.__tamanho_arquivo = None

        def __str__(self):
            return (f"Ebook: {self._titulo}\n"
                    f"Autor: {self._autor}\n"
                    f"Ano: {self._ano}\n"
                    f"MB: {self.__tamanho_arquivo}")

        @property
        def tamanho_arquivo(self):
            return self.__tamanho_arquivo

        @tamanho_arquivo.setter
        def tamanho_arquivo(self, valor):
            self.__tamanho_arquivo = valor

    livro = Livro(None, None, None)
    livro.titulo = input("Titulo: ").strip()
    livro.autor = input("Autor: ").strip()
    livro.ano = int(input("Ano: "))

    ebook = Ebook(livro.titulo, livro.autor, livro.ano)
    ebook.tamanho_arquivo = int(input("Indique o tamanho do arquivo (MB): "))

    print()
    print(ebook)


if __name__ == "__main__":
    main()
