def divisao(a, b):
    div = a / b
    print(f"A divisão de {a} por {b} é {div}")


try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(divisao(num1, num2))

except ZeroDivisionError:
    print(f"ERRO! NÃO É POSSIVEL DIVIDIR POR 0")

except ValueError:
    print("O Utilizador não digitou números")

except KeyboardInterrupt:
    print("O programa foi fechado inesperadamente")

else:
    print("A divisão é possivel.")

finally:
    print("TERMINOU!")
