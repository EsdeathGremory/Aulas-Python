listaDados = []
continuar = "S"

while continuar == "S":
    dados = dict()
    dados['nome'] = input("Nome da Pessoa: ")
    dados['sexo'] = input(f"Género [F/M]: ").upper()
    dados['idade'] = int(input(f"Idade de {dados["nome"]}: "))
    listaDados.append(dados)
    continuar = input("Deseja continuar? [S/N]: ").upper()


totalregistos = 0
somaIdades = 0
mulheres = 0
somaIdadesH = 0
homens = 0
ListaHomens = []
HAM = 0
for dados in listaDados:
    totalregistos += 1
    somaIdades += dados["idade"]
    if dados["sexo"] == "F":
        mulheres += 1
    if dados["sexo"] == "M":
        homens += 1
        somaIdadesH += dados["idade"]
        ListaHomens.append(dados)

mediaIdades = somaIdades / totalregistos
mediaHomem = HAM / homens

for homen in ListaHomens:
    if homen["idade"] > mediaHomem:
        HAM += 1

print()
print(f"Total de registos: {totalregistos}")
print(f"Média de Idades: {mediaIdades}")
print(f"Mulheres Registadas: {mulheres}")
print(f"Homens com idade acima da média: {HAM}")
