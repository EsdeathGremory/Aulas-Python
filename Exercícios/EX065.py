from datetime import datetime


def carta_conducao(data):
    idade = datetime.today().year - data
    if idade >= 18:
        return f"A pessoa introduzida pode tirar a carta de condução porque tem {idade} anos."

    elif 18 > idade >= 16:
        return f"A pessoa introduzia precisa de autorização porque tem {idade} anos."

    else:
        return f"A pessoa introduzida não pode tirar a carta de condução porque tem {idade} anos."


ano_nascimento = int(input("Insira o ano de nascimento:"))
print(carta_conducao(ano_nascimento))


