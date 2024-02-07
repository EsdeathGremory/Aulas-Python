# Exemplo 'for'
'''num = 9

for c in range(0, 10):
    print(num, "x", c + 1, "=", num * (c+1))'''

''' # De 2 em 2
i = 1
f = 10
salto = 2

for MichaelJackson in range (i, f, salto):
    print(MichaelJackson)'''

'''tentativas = 3
mensagem = "Bem Vindo"
password = "password"

for c in range(0, tentativas):
    entrada = input("Insira a password: ")
    if entrada == password:
        print(mensagem)
    else:
        tentativas = tentativas + 1
        print("Tente novamente...\n")
    
    if tentativas == 3:
        print("Utilizador Bloqueado")'''
