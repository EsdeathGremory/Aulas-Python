# EX047

c = 0

count1 = 0
count2 = 0

equacao = str(input("Insira uma equação:"))

for c in equacao:
    if c == "(":
        count1 += 1

    elif c == ")":
        count2 += 1

if count1 != count2:
    print("A sua equação têm os parênteses errados!")

else:
    print("A sua equação está correta!")
