# EX025

frase = input("Escreva uma frase:").strip().lower()

palindromo = "".join(frase.split())

if (palindromo == palindromo[::-1]):
    print("A sua frase é um palíndromo.")

else:
    print("A sua frase não é um palíndromo.")