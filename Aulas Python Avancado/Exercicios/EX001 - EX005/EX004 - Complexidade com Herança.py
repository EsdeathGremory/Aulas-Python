from Modelos.Class import Livro, Ebook, Biblioteca


def main():
    i = 0
    biblioteca = Biblioteca()
    livro = Livro(None, None, None)
    ebook = Ebook(livro.titulo, livro.autor, livro.ano)
    while i != 3:

        livro.titulo = input("Titulo: ").strip()
        livro.autor = input("Autor: ").strip()
        livro.ano = int(input("Ano: "))

        ebook.tamanho_arquivo = int(input("Indique o tamanho do arquivo (MB): "))

        biblioteca.add_livro(livro)
        biblioteca.add_livro(ebook)
        i += 1

    biblioteca.lista_livros()


if __name__ == "__main__":
    main()
