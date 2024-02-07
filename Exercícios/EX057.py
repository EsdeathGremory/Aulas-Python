jogadores = []
continuar = "S"
while continuar == "S":
    jogador = dict()
    jogador["Nome"] = input("Insira o nome:")
    jogador["Jogos"] = int(input("Insira o número de jogos: "))
    jogador["Golos"] = int(input("Insira o número de golos: "))
    jogador["Média de Golos por jogo"] = jogador["Golos"] / jogador["Jogos"]
    print(jogador)

    jogadores.append(jogador)
    continuar = input("Deseja continuar? [s/n]").upper()

print()
escolher = input("Nome do jogador que deseja ver os dados: ")
print()
for i in jogadores:
    if i["Nome"] == escolher:
        print(f"O jogador {i["Nome"]} tem uma média de {i["Média de Golos por jogo"]} golos por jogo.")
