print("Exemplo 1:")


def soma(a, b):
    """
    -> Esta função imprime no ecrã a soma entre as  variáveis
    :param a: primeiro número da soma
    :param b: segundo número da soma
    :return:
    """
    s = a + b
    print(f"A soma entre {a} e {b} é igual a: {s}")


soma(10, 15)
print()
"""help(soma)"""


print("Exemplo 2:")


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


resultado = soma(c=2, a=1, b=3)
resultado2 = soma(75, 45, 52)
print(f"A primeira soma vale {resultado} e a segunda vale {resultado2}.")
