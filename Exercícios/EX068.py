def turma(*dados):
    dturma = {"Quantidade de Notas": [], "Maior Nota": [], "Média da turma": [], "Situação": []}
    media = 0
    maior = 0
    soma = 0
    dturma["Quantidade de Notas"] = len(dados)
    for i in range(len(notas)):
        if i > maior:
            maior = i
        soma = i + soma



    media = soma / dturma["Quantidade de Notas"]
    dturma["Maior Nota"] = maior
    dturma["Média da turma"] = media




notas = list()
while True:
    num = int(input("Insira uma Nota: "))
    c = input("Continuar? [S/N]").strip().upper()
    if not c == "N":
        notas.append(num)
    else:
        break
