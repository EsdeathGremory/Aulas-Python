def media(*calculo):
    soma = 0
    for i in calculo[0]:
        soma = soma + i

    media = soma / len(notas)
    if media >= 9.5:
        print(f"O aluno {nome} foi aprovado, com uma média de {media}.")
    else:
        print(f"O aluno {nome} não foi aprovado, porcausa de ter uma media de {media}.")


notas = list()
nome = input("Insira o nome do aluno: ")

while True:
    notas.append(int(input("Insira a nota: ")))
    continuar = input("Inserir outra nota? [S/N]: ").upper()
    if continuar == "N":
        break

media(notas)
