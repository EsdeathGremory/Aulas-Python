def divisao(a, b):
    div = a / b
    return div


try:
    num1 = int(input("Introduza o primeiro número: "))
    num2 = int(input("Introduza o segundo número: "))
    print(f"{num1} / {num2} = {divisao(num1, num2)}")

except ZeroDivisionError:
    print(f"Não é possivel dividir por 0.")

except ValueError:
    print(f"A informação introduzida não é valida.")

finally:
    print("TERMINOU!")
