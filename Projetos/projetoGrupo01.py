# Leitura de dados
peso = float(input("Insira o seu peso:"))
altura = float(input("Insira a sua altura:"))

# Calculo do IMC
IMC = peso / (altura * altura)

# Apresentação dos calculos
if IMC < 18.5:
    print("Está a baixo do peso")

elif 18.5 <= IMC <= 24.9:
    print("Está com peso normal")

elif 25.0 <= IMC <= 29.9:
    print("Sobrepeso")

elif 30.0 <= IMC <= 34.9:
    print("Obesidade grau 1")

elif 35.0 <= IMC <= 39.9:
    print("Obesidade grau 2")

elif IMC > 40.0:
    print("Obesidade grau 3 (Obesidade morbida)")
