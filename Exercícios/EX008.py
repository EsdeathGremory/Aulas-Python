# EX008

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