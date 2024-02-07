# EX034

# Recolha de dados
print("[1] - Inserir Notas")
print("[2] - Sair")
opcao = int(input("Opção:"))

somaNotas = 0
count = 0

#Calculo da média
while opcao != 2:
    nota = float(input("Introduza a Nota:"))
    somaNotas = nota + somaNotas
    count += 1

    print("[1] - Inserir outra nota:")
    print("[2] - Média")
    opcao = int(input("Opção:"))

media = somaNotas / count
print(f"A média das notas inseridas é {media}.")
