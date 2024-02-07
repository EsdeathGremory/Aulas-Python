"""# Passagem de ano EX021
from time import sleep
import winsound
frequency = 2500
duration = 1000
winsound.Beep(frequency, duration)
for c in range(10, 0, -1):
    print(c)
    sleep(1)

    if c == 1:
        print("Feliz ano novo!")"""

"""# Numeros pares entre 1 e 100 EX022
for num in range(1, 100, 2):
    print(num + 1)"""

"""# Tabuada de um numero introduzido pelo utilizador EX023

num = int(input("Insira um numero:"))

for c in range (0, 10):
    print(num, "x", c + 1, "=", num*(c + 1))"""


"""# Ler e indicar se é numero primo EX024

num = int(input("Insira um numero:"))
tot = 0

for A in range (1, num+1):
    if num % A == 0:
        tot += 1

if tot == 2:
    print(f"O numero {num} é primo, foi divisivel {tot} vezes.")

else:
    print(f"O numero {num} não é primo, foi divisivel {tot} vezes.")"""


""" # EX025

frase = input("Escreva uma frase:").strip().lower()

palindromo = "".join(frase.split())

if (palindromo == palindromo[::-1]):
    print("A sua frase é um palíndromo.")

else:
    print("A sua frase não é um palíndromo.")"""


"""# EX026
from datetime import date
data_atual = date.today().year
count = 0
count2 = 0
for a in range(0, 7):
    anoNasc = int(input("Insira o ano de nascimento:"))

    idade = data_atual - anoNasc

    if idade >= 18:
        count = count + 1

    else:
        count2 = count2 + 1

print(f"{count} pessoas são maiores de idade.")
print(f"{count2} pessoas são menores de idade.")"""


"""# EX027

maior_idade = 0
menor_idade = 0
for a in range(0, 10):
    idade = int(input("Insira uma idade:"))

    if maior_idade <= idade:
        maior_idade = idade

    elif menor_idade == 0 or menor_idade >= idade:
        menor_idade = idade

print(f"A maior idade introduzida foi {maior_idade}.")
print(f"A menor idade introduzida foi {menor_idade}.")"""


"""# Exemplo While
opcao = 0

while opcao != 4:
    print("[1] - Registar pessoas")
    print("[2] - Numero de pessoas registadas")
    print("[3] - Apagar um registo")
    print("[4] - Sair")
    print("Qual a sua opção")
    opcao = int(input("---------->"))

    if opcao == 1:
        nome = input("Digite o nome da pessoa:")
        idade = int(input("Digite a idade da pessoa:"))
        print(f"{nome} registado com sucesso.")

    elif opcao == 2:
        print("Há X pessoas registadas.")

    elif opcao == 3:
        print("Um registo foi apagado.")

    if opcao < 1 or opcao > 4:
        print("Seu burro!")
        break

print("Obrigado e volte sempre.")"""

"""# EX028
count = 0

while count != 3:
    if count == 0:
        print("A construção da Torre Eiffel foi concluída em 31 de março de 1887?")
        print("[V] - Verdadeiro")
        print("[F] - Falso")
        resposta = input("----->").upper()
        print(resposta)

        while resposta not in 'VF':
            resposta = input("Apenas ensira [V] ou [F]").upper()

            if resposta == 'F':
                print("Correto!")
                count += 1
            elif resposta == 'V':
                print("Errado!")
                resposta = input("Tente novamente:").upper()
                if resposta == 'F':
                    print("Correto!")
                    count += 1

    elif count == 1:
        print("O relâmpago é visto antes de ser ouvido porque a luz viaja mais rápido que o som.?")
        print("[V] - Verdadeiro")
        print("[F] - Falso")
        resposta = input("----->").upper()

        while resposta not in 'VF':
            resposta = input("Apenas ensira [V] ou [F]").upper()

        if resposta == 'V':
            print("Correto!")
            count += 1
        elif resposta == 'F':
            print("Errado!")
            resposta = input("Tente novamente:").upper()
            if resposta == 'V':
                print("Correto!")
                count += 1

    else:
        print("O Monte Fuji é a montanha mais alta do Japão.?")
        print("[V] - Verdadeiro")
        print("[F] - Falso")
        resposta = input("----->").upper()

        while resposta not in 'VF':
            resposta = input("Apenas ensira [V] ou [F]").upper()

        if resposta == 'V':
            print("Correto!")
            count += 1
        elif resposta == 'F':
            print("Errado!")
            resposta = input("Tente novamente:").upper()
            if resposta == 'V':
                print("Correto!")
                count += 1"""

""" # EX029
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

print(f"Acertou no número correto depois de {count} tentativas.")"""

