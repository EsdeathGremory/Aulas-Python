# Ler e indicar se é numero primo EX024

num = int(input("Insira um numero:"))
tot = 0

for A in range (1, num+1):
    if num % A == 0:
        tot += 1

if tot == 2:
    print(f"O numero {num} é primo, foi divisivel {tot} vezes.")

else:
    print(f"O numero {num} não é primo, foi divisivel {tot} vezes.")