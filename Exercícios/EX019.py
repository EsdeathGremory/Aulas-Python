# EX019

# Calculo do numero random
import random
numPC = random.randint(0, 7)

# Leitura de dados
numUtilizador = int(input("Escolha um numero de 0 a 7: "))

# Apresentar no ecrã
if (numUtilizador < 0 or numUtilizador > 7):
    numUtilizador = int(input("Insira um número válido: "))

if (numUtilizador == numPC):
    print("Victory")

else:
    print("Defeat")
    print(f"O número era {numPC}")