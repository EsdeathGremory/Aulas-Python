"""# EX009
nome = input("Insira o seu nome:").strip()
print("Maiúsculas: {}".format(nome.upper()))
print("Minúsculas: {}".format(nome.lower()))

print("O seu nome tem {} caracteres".format(len(nome) - nome.count(" ")))

pNome = nome.split()

print("O seu primeiro nome é {} e tem {} caracteres".format( pNome[0], len(pNome[0])))
"""

"""# EX 010
num = int(input("Insira um numero de 0 a 9999:"))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))"""

"""# EX 011

frase = input("Escreva uma frase:").upper().strip()

print("A letra 'A' aparece {} vezes.".format(frase.count("A")))
print("O primeiro 'A' está na posição: {}.".format(frase.find("A") + 1))
print("O ultimo 'A' está na posição: {}.".format(frase.rfind("A") + 1))"""

"""# EX 012

nome = input("Insira o seu nome:").strip()

sNome = nome.split()
primeiraLetra = sNome[0][0]

print("Olá {}, o seu registo está completo.".format(nome))
print("O seu email é {}.{}.edu@empresa.pt".format(primeiraLetra.lower(), sNome[1].lower()))
"""

"""# EX013
palavra = "Python"

arvalap = palavra[5] + palavra[4] + palavra[3] + palavra[2] + palavra[1] + palavra[0]
print(arvalap)"""

"""# EX 014

speed = int(input("Insira a velucidade:"))

multa = 100 + ((speed - 80)*7)

if (speed > 80):
    print("Multado em:", multa, "€")

else:
    print("Não multado.")"""

"""
# EX015
numero = int(input("Insira um numero:"))

resto = numero % 2

if (resto == 0):
    print("Numero par.")

else:
    print("Numero impar.")
"""

""" # EX016

# Ler os dados
num1 = float(input("Insira a primeira nota:"))
num2 = float(input("Insira a segunda nota:"))
num3 = float(input("Insira a terceira nota:"))
num4 = float(input("Insira a quarta nota:"))
num5 = float(input("Insira a quinta nota:"))

# Calcular a media
media = (num1 + num2 + num3 + num4 + num5) / 5

# Apresentar os dados
if (media >= 9.5):
    print(f"Passou, com uma média de {media} valores.")

elif (media >= 8 and media < 9.5):
    print(f"Recuperação, com uma média de {media} valores.")

else:
    print(f"Reprovado, com uma média de {media} valores.")"""

"""
# EX017

# Ler os dados
num = int(input("Insira o numero:"))
print("")
print("[Binário] - 1")
print("[Octal] - 2")
print("[Hexadecimal] - 3")
conversao = int(input("Insira o número da opção desejada:"))

# Conversão dos dados e apresentação
if (conversao != 1 and conversao != 2 and conversao != 3):
    conversao = int(input("Insira uma opção válida:"))

if (conversao == 1):
    print(f"O número:{num}, em binário é:{bin(num)[2:]}.")

elif (conversao == 2):
    print(f"O número:{num}, em octal é:{oct(num)[2:]}.")

else:
    print(f"O número:{num}, em hexadécimal é:{hex(num)[2:].upper()}.")
"""

"""
# EX018

# Ler os dados
num1 = int(input("Insira o primeiro número:"))
num2 = int(input("Insira o segundo número:"))

# Apresentar no ecrã
if (num1 > num2):
    print("O primeiro número é maior;")

elif (num2 > num1):
    print("O segundo número é maior;")

else:
    print("Os números são iguais;")
"""

"""
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
"""
print("já está")