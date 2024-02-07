# EX028
count = 0

while count != 3:
    if count == 0:
        print("A construção da Torre Eiffel foi concluída em 31 de março de 1887?")
        print("[V] - Verdadeiro")
        print("[F] - Falso")
        resposta = input("----->").upper()
        print(resposta)

        while resposta not in 'VF':
            resposta = input("Apenas ensira [V] ou [F]").upper()

            if resposta == 'F':
                print("Correto!")
                count += 1
            elif resposta == 'V':
                print("Errado!")
                resposta = input("Tente novamente:").upper()
                if resposta == 'F':
                    print("Correto!")
                    count += 1

    elif count == 1:
        print("O relâmpago é visto antes de ser ouvido porque a luz viaja mais rápido que o som.?")
        print("[V] - Verdadeiro")
        print("[F] - Falso")
        resposta = input("----->").upper()

        while resposta not in 'VF':
            resposta = input("Apenas ensira [V] ou [F]").upper()

        if resposta == 'V':
            print("Correto!")
            count += 1
        elif resposta == 'F':
            print("Errado!")
            resposta = input("Tente novamente:").upper()
            if resposta == 'V':
                print("Correto!")
                count += 1

    else:
        print("O Monte Fuji é a montanha mais alta do Japão.?")
        print("[V] - Verdadeiro")
        print("[F] - Falso")
        resposta = input("----->").upper()

        while resposta not in 'VF':
            resposta = input("Apenas ensira [V] ou [F]").upper()

        if resposta == 'V':
            print("Correto!")
            count += 1
        elif resposta == 'F':
            print("Errado!")
            resposta = input("Tente novamente:").upper()
            if resposta == 'V':
                print("Correto!")
                count += 1