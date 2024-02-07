from datetime import date

anoatual = date.today().year


class Livro:
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano

    def __str__(self):
        return (f"Título: {self._titulo}\n"
                f"Autor: {self._autor}\n"
                f"Ano: {self._ano}\n")

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

    # EX005 - Sobrescrever Métodos em Herança
    def __str__(self):
        return (f"Ebook: {self._titulo}\n"
                f"Autor: {self._autor}\n"
                f"TAMANHO DO ARQUIVO: {self.__tamanho_arquivo}MB")

    @property
    def tamanho_arquivo(self):
        return self.__tamanho_arquivo

    @tamanho_arquivo.setter
    def tamanho_arquivo(self, valor):
        self.__tamanho_arquivo = valor


class Biblioteca:
    def __init__(self):
        self.livros = list()
        self.ebook = list()

    def add_livro(self, valor):
        self.livros.append(valor)

    def add_ebook(self, valor):
        self.ebook.append(valor)

    def lista_livros(self):
        for i in self.livros:
            print(i)

    def lista_ebook(self):
        for i in self.livros:
            print(i)
