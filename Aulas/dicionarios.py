"""aluno = {"Nome": "Cesar", "Média": 14}
print(f"O aluno {aluno['Nome']} tem a média de {aluno['Média']} valores.")

if aluno["Média"] >= 9.5:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"

print(aluno.items())"""

"""aluno = dict()

aluno["Nome"] = input("Digite o nome do aluno:")
aluno["EX001"] = int(input("Digite a nota do EX001:"))
aluno["EX002"] = int(input("Digite a nota do EX002:"))
aluno["EX003"] = int(input("Digite a nota do EX003:"))

print(aluno.items())

aluno["Média"] = (aluno["EX001"] + aluno["EX002"] + aluno["EX003"]) / 3

print(aluno.items())

del aluno["Média"]
print(aluno.items())"""

cidade = {"Nome": "Porto", "Código": "OPO", "Baixa": "Ribeira", "Rio": "Douro"}
cidade2 = {"Nome": "Lisboa", "Código": "LX", "Baixa": "Chiado", "Rio": "Tejo"}

pais = list()
pais.append(cidade)
pais.append(cidade2)

print(pais)

for k, v in cidade.items():
    print(f"O {k} é {v}")

for c in range(0, len(pais)):
    print(f"{pais[c]['Nome']}")
