def mensagem(msg):
    menssagem = f"---{msg}---"
    total_width = int(len(menssagem) / 2 + 1)
    print("*=" * total_width)
    print(menssagem)
    print("*=" * total_width)
    print()

def calculador_imc(idade, peso, altura):
    """
    -> esta função calcula o imc
    :param idade: idade da pessoa
    :param peso:  peso da pessoa
    :param altura:  altura da pessoa
    :return: retorna o imc da pessoa
    """
    i = round(peso / (altura * altura), 2)
    return i


def grau_obesidade(valor):
    """
    -> esta função informa o estado do utilizador.
    :param valor: imc do utilizador
    :return: valor associado ao imc
    """
    valor_imc = ""
    if valor < 18.5:
        valor_imc = "Abaixo do peso"
    elif valor <= 24.9:
        valor_imc = "Peso normal"
    elif valor <= 29.9:
        valor_imc = "Sobrepeso"
    elif valor <= 34.9:
        valor_imc = "Obesidade grau 1"
    elif valor <= 39.9:
        valor_imc = "Obesidade grau 2"
    elif valor >= 40.0:
        valor_imc = "Obesidade mórbida"
    return valor_imc


mensagem("Calculador de IMC")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
if altura >= 3:
    altura = altura / 100

imc = calculador_imc(idade, peso, altura)
imc_dados = grau_obesidade(imc)

print(f"O estado do utilizador é: {imc_dados}")
