# EX029
import random

# variáveis e número do pc
count = 0
numPC = random.randint(0, 10)

# Primeira tentativa:
resposta = int(input("Insira o numero:"))
count += 1

# Loop da resposta
while resposta != numPC:
    resposta = int(input("Tente novamente:"))
    count += 1

print(f"Acertou no número correto depois de {count} tentativas.")