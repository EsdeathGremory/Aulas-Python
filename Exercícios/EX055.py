jogador = dict()

jogador["Nome"] = input("Insira o nome:")
jogador["Jogos"] = int(input("Insira o número de jogos: "))
jogador["Golos"] = int(input("Insira o número de golos: "))
jogador["Média de Golos por jogo"] = jogador["Golos"] / jogador["Jogos"]

print(jogador)
