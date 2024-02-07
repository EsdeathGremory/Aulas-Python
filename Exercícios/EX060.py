from time import sleep

def contar(a, b, c):
    print(f"Contagem de {a} até {b}, de {c} em {c}: ")
    if a < b:
        num = a
        while num <= b:
            print(num, end=" ")
            num += c
            sleep(0.5)
    if a > b:
        num = a
        while num >= b:
            print(num, end=" ")
            num += -c
            sleep(0.5)


contar(1, 20, 2)
print()
print()
contar(10, 0, 1)

print()
print()
print("Contagem Personalizada")
num1 = int(input("Inicio: "))
num2 = int(input("Fim: "))
num3 = int(input("De: "))

print()
contar(num1, num2, num3)



