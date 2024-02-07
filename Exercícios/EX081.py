class Livro:
    def __init__(self):
        print("A criar livro...")
        self.__titulo = ""
        self.__ano = 0
        self.__autor = ""
        self.__disponibilidade = False

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade


print("-- BIBLIOTECA --")
Esdeath = input("Clique para adicionar um novo livro...")

titulo = input("TÍTULO: ")
ano = int(input("ANO: "))
autor = input("AUTOR: ")
disponibilidade = input("DISPONIBILIDADE (S/N): ").strip().upper()

if disponibilidade == "S":
    disponibilidade = True

else:
    disponibilidade = False

livro = Livro()

livro.titulo = titulo
livro.ano = ano
livro.autor = autor
livro.disponibilidade = disponibilidade

print()
print(livro.titulo)
print(livro.ano)
print(livro.autor)
print(livro.disponibilidade, '\n')

opcao = int(input("[6] - Editar Dados\n[5] - Sair\n-->"))
while opcao != 5:
    opcao = int(input("[1] - Título\n[2] - Ano\n[3] - Autor\n[4] - Disponibilidade\n[5] - Sair\n-->"))
    if opcao == 1:
        livro.titulo = input("Insira o novo título: ")

    if opcao == 2:
        livro.ano = int(input("Insira o novo ano: "))

    if opcao == 3:
        livro.autor = input("Insira o novo autor: ")

    if opcao == 4:
        disponibilidade = input("Insira a disponibilidade: ").strip().upper()
        if disponibilidade == "S":
            livro.disponibilidade = True

        else:
            livro.disponibilidade = False

print()
print(livro.titulo)
print(livro.ano)
print(livro.autor)
print(livro.disponibilidade)

