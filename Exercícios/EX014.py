# EX 014

speed = int(input("Insira a velucidade:"))

multa = 100 + ((speed - 80)*7)

if (speed > 80):
    print("Multado em:", multa, "€")

else:
    print("Não multado.")