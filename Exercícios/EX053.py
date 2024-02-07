import random
import operator

dado = {"Nome": [], "Número": []}

for i in range(0, 4):
    dado["Nome"].append(f"Player {i+1}")
    dado["Número"].append(random.randint(1, 6))

vez = dict(sorted(zip(dado["Nome"], dado["Número"]), key=lambda ordem: ordem[1]))
print(vez)
