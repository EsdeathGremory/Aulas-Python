# EX042
game = ("Cyberpunk2077: 40", "Mad Max: 5")
sortedGame = sorted(game, key=lambda valor: int(valor.split(":")[1]))

print("Jogo ---- Preço")

for ordem in sortedGame:
    print(f"{ordem.split(': ')[0]} ---- {ordem.split(': ')[1]}€")
