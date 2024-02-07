"""# EX020

# Escolha de pedra, papel ou tesoura do pc
import random

numPC = random.randint(1, 3)

# Escolha do pedra, papel, tesoura do utilizador

print("[Pedra] - 1")
print("[Papel] - 2")
print("[Tesoura] - 3")
print("")
print("Escolha do PC:", numPC)
numU = int(input("Escolha uma das opções:"))

if (numPC == numU):
    print("Draw")

elif (numPC - numU == 2 or numPC - numU == -1):
    print("Victory")

else:
    print("Defeat")"""

