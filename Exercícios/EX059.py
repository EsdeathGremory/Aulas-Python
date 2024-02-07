def mostre(msg):
    i = 0
    while i < (6 + len(msg)):
        print("", end="-")
        i += 1
    print()
    print(f"---{msg}---")
    i = 0
    while i < (6 + len(msg)):
        print("", end="-")
        i += 1


msgg = input("Escreva uma mensagem: ")
mostre(msgg)
