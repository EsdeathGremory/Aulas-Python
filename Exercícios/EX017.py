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