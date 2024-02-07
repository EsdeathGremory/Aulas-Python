"""# EX001
print("Olá mundo! \n")

# EX002
print("---------------------------")
print("------Seja-bem-vindo!------")
print("--------------------------- \n")

# EX003
num1 = int(input("Insira o primeiro numero:"))
num2 = int(input("Insira o segundo numero:"))

soma = num1 + num2

print("A soma de", num1, "com", num2, "é:", soma)
print("")

# EX004
num = int(input("Insira um numero:"))

antecessor = num - 1
sucessor = num + 1

print("O antecessor do numero", num, "é", antecessor, "e o sucessor é", sucessor)
"""

"""# EX005

# Ler numeros do utilizador
num1 = int(input("Insira o primeiro numero:"))
num2 = int(input("Insira o segundo numero:"))

# Estruturar variaveis e cálculos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
# // é devisão inteira
divisao = num1 / num2
resto = num1 % num2

# Apresentar resultados no ecra
print("")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Resto:", resto)

"""

""" # EX006
# Ler os valores
num1 = float(input("Insira a primeira nota:"))
num2 = float(input("Insira a segunda nota:"))
num3 = float(input("Insira a terceira nota:"))
num4 = float(input("Insira a quarta nota:"))
num5 = float(input("Insira a quinta nota:"))

# Calculos
media = (num1 + num2 + num3 + num4 + num5) / 5

# Apresenta no ecrã
print("")
print("A média é:", media)

"""

""" EX007
# Leitura de dados
ano_nascimento = int(input("Insira o seu ano de nascimento:"))
ano_atual = int(input("Insira o ano atual:"))

# Calculos
idade = ano_atual - ano_nascimento

# Apresenta no ecrã
print("A idade do utilizador é:", idade, "anos.")
"""

"""# EX008

# Ler dados
km_percorridos = float(input("Insira o numero de Km percorridos:"))
num_dias = float(input("Insira o numero de dias que o carro foi alugado:"))

# Calculos
custo_km = 0.456
custo_dias = 60
preco_total = (km_percorridos * custo_km) + (num_dias * custo_dias)

# Apresenta no ecrã
print("")
print("O total a pagar é:", preco_total, "$")

"""