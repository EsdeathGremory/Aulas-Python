nome = input("Insira o Nome:")
print("Maiúsculas: {}".format(nome.upper()))
print("Minúsculas: {}".format(nome.lower()))

nomes = nome.split()

print("O seu nome tem {} letras.".format(len(nome) - nome.count(" ")))

print("Numero de letras do primeiro nome: {}".format(len(nomes[0])))