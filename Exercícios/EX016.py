# EX016

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
    print(f"Reprovado, com uma média de {media} valores.")