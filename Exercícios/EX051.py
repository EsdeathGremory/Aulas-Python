import random

vezes = int(input("Quantos palpites quer?"))

for i in range(0, vezes):
    palpite = [[], []]
    for a in range(0, 5):
        while True:
            num = random.randint(1, 50)
            if num not in palpite[0]:
                palpite[0].append(num)
                break

    for b in range(0, 2):
        while True:
            num = random.randint(1, 12)
            if num not in palpite[1]:
                palpite[1].append(num)
                break

    print(palpite)
