# funções
def insere_linha():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")

def cabecalho(msg):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(msg)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def soma(a, b):
    s = a + b
    print(f"A soma entre {a} e {b} é igual a: {s}")

def conta_numeros(*num):
    print(f"Inseriu: {len(num)} numeros")
    for numeros in num:
        print(f"{numeros}", end=" ")

# Programa Principal
print("Código com prints")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Olá mundo")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()

print("Código com funções:")
insere_linha()
print("Olá Mundo")
insere_linha()
print()

cabecalho("Olá Mundo")
cabecalho("Olá turma")
cabecalho("Coisas")

soma(4, 4)
soma(13, 15)

conta_numeros(1, 2, 3, 4, 5, 6)
conta_numeros(1, 3, 5)
conta_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9)
