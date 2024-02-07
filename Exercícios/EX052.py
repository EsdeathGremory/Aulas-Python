aluno = dict()
aluno["Nome"] = input("Digite o nome do aluno:")
aluno["Média"] = int(input(f"Insira a média do {aluno['Nome']}:"))

if aluno["Média"] >= 9.5:
    aluno["Situação"] = "Aprovado"

else:
    aluno["Situação"] = "Reprovado"

print(aluno)