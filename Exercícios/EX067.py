def input2(num=0):
    num = input("Insira um número inteiro: ")
    while True:
        if num == str:
            print(f"O valor introduzido não é um número inteiro!")
            num = input("Insira um número inteiro: ")


        elif not num.isnumeric():
            print(f"O valor introduzido não é um número inteiro!")
            num = input("Insira um número inteiro: ")

        else:
            print(f"O valor introduzido é um número inteiro!")
            break


input2()
