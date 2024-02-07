import datetime


def registo_utilizador():
    """
    -> Esta função cria um dicionário que faz o registo do utilizador, o livro requisitado,
    e dá uma data de entrega prevista.
    -> Cria um ficheiro .txt onde os dados são guardados.

    -> This function creates a dictionary that returns the User, the books requested by the User, and gives a estimated
    date to return the book
    -> Creates a .txt file where the data is saved.

    :return:
    """
    utilizador = dict()
    dia = datetime.date.today() + datetime.timedelta(days=7)

    utilizador["Nome do utilizador"] = str(input("Insira o nome: "))
    utilizador["Nome do livro"] = str(input("Insira o nome do livro: "))
    utilizador["Data de devolução prevista"] = dia

    with open('registo_utilizador.txt', 'a') as data:
        data.write(str(utilizador) + "\n")

    for i, v in utilizador.items():
        print(f"{i}: {v}")


registo_utilizador()

"""
-> Para ler o txt file

with open('registo_utilizador.txt') as f:
    contents = f.read()
    print(contents)"""
