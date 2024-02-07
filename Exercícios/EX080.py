class Alunos:
    def __init__(self, nome, notas):
        self.__nome = nome
        self.__notas = notas

    def media(self):
        c = 0
        soma = 0
        for i in self.__notas:
            c += 1
            soma = soma + i
        media = soma / c
        return media

    def estado_aluno(self, valor):
        if valor >= 9.5:
            print("O aluno esta aprovado.")
        else:
            print("O aluno esta reprovado.")


lista_notas = list()
nome_aluno = input("Insira o nome do aluno: ")
sair = None
while sair != 'Y':
    nota = float(input("Insira a nota do aluno: "))
    lista_notas.append(nota)
    sair = input("Para de inserir notas?\n[Y] - Sair [N] - Continuar\n-->").strip().upper()

aluno = Alunos(nome_aluno, lista_notas)

print(f"A média do aluno é:{aluno.media()}")
aluno.estado_aluno(aluno.media())
